"""
Sentinel Protocol — API Server
Implements the endpoints specified in docs/api/endpoints.md.

Run: uvicorn prototype.python.api.server:app --reload
Requires: pip install fastapi uvicorn
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ..cortex.ingestion import MessageIngestor
from ..cortex.scoring import score_message
from ..energy.biometrics import calculate_capacity
from ..energy.fatigue import calculate_dfs
from ..negotiation.leverage import DealContext, calculate_leverage, generate_offer, scarcity_signal
from ..persona.masks import select_mask

app = FastAPI(
    title="The Sentinel Protocol API",
    version="0.1.0",
    description="Reference service implementation of docs/api/endpoints.md",
)

SCHEMA_DIR = Path(__file__).resolve().parents[3] / "schemas"


def _load_schema(name: str) -> dict:
    with open(SCHEMA_DIR / name) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Request/response models (mirror schemas/*.schema.json — see docs/api/schemas.md)
# ---------------------------------------------------------------------------

class IngestRequest(BaseModel):
    raw_data: str
    headers: dict = Field(default_factory=dict)


class ScoreRequest(BaseModel):
    clean_text: str
    fingerprint: str
    metadata: dict = Field(default_factory=dict)
    crm_value: float | None = None
    days_since_last_contact: float = 0.0
    objectives: list[str] = Field(default_factory=list)


class DraftRequest(BaseModel):
    tier: str
    relationship_stage: str = "established"
    context: str = "external"
    detected_intent: str | None = None


class OfferRequest(BaseModel):
    urgency: float
    uniqueness: float
    substitute_count: int
    time_buffer_days: int
    base_price: float
    real_capacity_remaining: int | None = None
    real_deadline: str | None = None


class CapacityRequest(BaseModel):
    hrv_current: float
    baseline_hrv: float
    sleep_score: float


class FatigueRequest(BaseModel):
    input_toxicity: float
    switching_cost: float
    cognitive_load: float


# ---------------------------------------------------------------------------
# Endpoints — see docs/api/endpoints.md for the full contract
# ---------------------------------------------------------------------------

@app.post("/v1/ingest")
def ingest(req: IngestRequest):
    ingestor = MessageIngestor(req.raw_data, headers=req.headers)
    result = ingestor.run()
    return {
        "clean_text": result.clean_text,
        "fingerprint": result.fingerprint,
        "metadata": result.metadata,
        "received_at": result.received_at.isoformat(),
    }


@app.post("/v1/score")
def score(req: ScoreRequest):
    from ..cortex.ingestion import IngestedMessage

    message = IngestedMessage(
        clean_text=req.clean_text, fingerprint=req.fingerprint, metadata=req.metadata
    )
    scored = score_message(
        message,
        crm_value=req.crm_value,
        days_since_last_contact=req.days_since_last_contact,
        objectives=req.objectives,
    )
    result = {
        "fingerprint": scored.fingerprint,
        "priority_score": scored.priority_score,
        "tier": scored.tier,
        "factors": scored.factors,
        "explanation": scored.explanation,
        "scored_at": scored.scored_at.isoformat(),
        "model_version": scored.model_version,
    }
    return result


@app.post("/v1/draft/mask")
def draft_mask(req: DraftRequest):
    """Returns the selected mask for a drafting request — see
    docs/persona/masks.md. Full draft generation requires an LLM
    provider key and is intentionally not wired to a live model call
    in this reference server (docs/deployment/local.md)."""
    mask = select_mask(
        tier=req.tier,
        relationship_stage=req.relationship_stage,
        context=req.context,
        detected_intent=req.detected_intent,
    )
    return {"mask": mask, "prompt_spec": f"prompts/{mask}.md"}


@app.post("/v1/negotiation/offer")
def negotiation_offer(req: OfferRequest):
    context = DealContext(
        urgency=req.urgency,
        uniqueness=req.uniqueness,
        substitute_count=req.substitute_count,
        time_buffer_days=req.time_buffer_days,
    )
    offer = generate_offer(context, base_price=req.base_price)
    signal = scarcity_signal(req.real_capacity_remaining, req.real_deadline)
    return {
        "price_multiplier": offer.price_multiplier,
        "rationale": offer.rationale,
        "mask": offer.mask,
        "leverage_score": offer.leverage_score,
        "scarcity_signal": signal,  # None if no real constraint — never fabricated
    }


@app.post("/v1/energy/capacity")
def energy_capacity(req: CapacityRequest):
    capacity = calculate_capacity(req.hrv_current, req.baseline_hrv, req.sleep_score)
    return {
        "capacity_score": capacity.value,
        "hrv_ratio": capacity.hrv_ratio,
        "is_depleted": capacity.is_depleted,
    }


@app.post("/v1/energy/fatigue")
def energy_fatigue(req: FatigueRequest):
    fatigue = calculate_dfs(req.input_toxicity, req.switching_cost, req.cognitive_load)
    return {"dfs": fatigue.value, "focus_mode_triggered": fatigue.focus_mode_triggered}


@app.get("/v1/schemas/{schema_name}")
def get_schema(schema_name: str):
    """Serves the canonical JSON Schemas from schemas/, per
    docs/api/schemas.md — keeps a single source of truth."""
    try:
        return _load_schema(f"{schema_name}.schema.json")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Schema not found")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
