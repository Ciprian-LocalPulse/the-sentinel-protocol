from fastapi.testclient import TestClient

from prototype.python.api.server import app

client = TestClient(app)


def test_healthz():
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_ingest_endpoint():
    resp = client.post(
        "/v1/ingest",
        json={"raw_data": "<p>Hello there</p>", "headers": {"From": "a@b.com"}},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["clean_text"] == "Hello there"
    assert len(body["fingerprint"]) == 64


def test_score_endpoint_returns_explainable_output():
    resp = client.post(
        "/v1/score",
        json={
            "clean_text": "This is urgent! Need this ASAP.",
            "fingerprint": "a" * 64,
            "crm_value": 50000,
            "days_since_last_contact": 2,
        },
    )
    assert resp.status_code == 200
    body = resp.json()
    assert "explanation" in body
    assert set(body["factors"].keys()) == {"FC", "EV", "TD", "SA"}


def test_draft_mask_boundary_request_returns_firewall():
    resp = client.post(
        "/v1/draft/mask",
        json={"tier": "P2", "detected_intent": "boundary_request"},
    )
    assert resp.status_code == 200
    assert resp.json()["mask"] == "firewall"


def test_negotiation_offer_no_fabricated_scarcity():
    resp = client.post(
        "/v1/negotiation/offer",
        json={
            "urgency": 5,
            "uniqueness": 5,
            "substitute_count": 3,
            "time_buffer_days": 10,
            "base_price": 1000,
        },
    )
    assert resp.status_code == 200
    # No real_deadline / real_capacity_remaining supplied -> must be None
    assert resp.json()["scarcity_signal"] is None


def test_negotiation_offer_honest_scarcity_with_real_constraint():
    resp = client.post(
        "/v1/negotiation/offer",
        json={
            "urgency": 5,
            "uniqueness": 5,
            "substitute_count": 3,
            "time_buffer_days": 10,
            "base_price": 1000,
            "real_capacity_remaining": 2,
            "real_deadline": "2026-09-01",
        },
    )
    assert resp.status_code == 200
    assert "2026-09-01" in resp.json()["scarcity_signal"]


def test_energy_capacity_endpoint():
    resp = client.post(
        "/v1/energy/capacity",
        json={"hrv_current": 52, "baseline_hrv": 65, "sleep_score": 80},
    )
    assert resp.status_code == 200
    assert resp.json()["capacity_score"] == 0.64


def test_get_schema_endpoint():
    resp = client.get("/v1/schemas/analysis")
    assert resp.status_code == 200
    assert resp.json()["title"] == "ScoredMessage"


def test_get_schema_endpoint_404_for_unknown():
    resp = client.get("/v1/schemas/does-not-exist")
    assert resp.status_code == 404
