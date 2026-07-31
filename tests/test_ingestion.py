from prototype.python.cortex.ingestion import MessageIngestor


def test_sanitize_strips_html_tags():
    ingestor = MessageIngestor("<p>Hello <b>world</b></p>")
    assert ingestor.sanitize() == "Hello world"


def test_sanitize_strips_boilerplate():
    raw = "Real content here.\nDisclaimer: This email is confidential and blah blah."
    ingestor = MessageIngestor(raw)
    cleaned = ingestor.sanitize()
    assert "Real content here." in cleaned
    assert "Disclaimer" not in cleaned


def test_fingerprint_is_deterministic():
    ingestor = MessageIngestor("Same text")
    fp1 = ingestor.fingerprint("Same text")
    fp2 = ingestor.fingerprint("Same text")
    assert fp1 == fp2
    assert len(fp1) == 64  # sha256 hex length


def test_fingerprint_differs_for_different_text():
    ingestor = MessageIngestor("")
    assert ingestor.fingerprint("A") != ingestor.fingerprint("B")


def test_extract_metadata_parses_sender_domain():
    ingestor = MessageIngestor("body", headers={"From": "client@example.com"})
    metadata = ingestor.extract_metadata()
    assert metadata["sender_domain"] == "example.com"


def test_extract_metadata_defaults_when_headers_missing():
    ingestor = MessageIngestor("body")
    metadata = ingestor.extract_metadata()
    assert metadata["sender_domain"] == ""
    assert metadata["priority_header"] == "3 (Normal)"


def test_run_returns_full_ingested_message():
    ingestor = MessageIngestor(
        "<p>Urgent: please respond</p>", headers={"From": "a@b.com"}
    )
    result = ingestor.run()
    assert result.clean_text == "Urgent: please respond"
    assert len(result.fingerprint) == 64
    assert result.metadata["sender_domain"] == "b.com"
