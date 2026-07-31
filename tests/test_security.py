from prototype.python.security.vault import IronVault, Scrubber


def test_iron_vault_roundtrip():
    key = IronVault.generate_key()
    vault = IronVault(key)
    ciphertext = vault.lock("sensitive business data")
    assert ciphertext != b"sensitive business data"
    assert vault.unlock(ciphertext) == "sensitive business data"


def test_iron_vault_different_keys_cannot_decrypt():
    key1 = IronVault.generate_key()
    key2 = IronVault.generate_key()
    vault1 = IronVault(key1)
    vault2 = IronVault(key2)
    ciphertext = vault1.lock("secret")
    try:
        vault2.unlock(ciphertext)
        assert False, "Should have raised an error"
    except Exception:
        pass


def test_scrubber_tokenizes_consistently():
    scrubber = Scrubber()
    t1 = scrubber.tokenize("John Smith", kind="PERSON")
    t2 = scrubber.tokenize("John Smith", kind="PERSON")
    assert t1 == t2
    assert t1.startswith("[PERSON_")


def test_scrubber_detokenize_restores_original():
    scrubber = Scrubber()
    token = scrubber.tokenize("Acme Corp", kind="ORG")
    text = f"The deal with {token} is progressing."
    restored = scrubber.detokenize(text)
    assert restored == "The deal with Acme Corp is progressing."


def test_scrubber_different_values_get_different_tokens():
    scrubber = Scrubber()
    t1 = scrubber.tokenize("Alice")
    t2 = scrubber.tokenize("Bob")
    assert t1 != t2
