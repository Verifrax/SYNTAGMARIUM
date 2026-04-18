import json
from pathlib import Path

def test_continuity_transfer_object_minimum():
    p = Path("continuity/objects/current/continuity-transfer-0001.json")
    data = json.loads(p.read_text())

    assert data["object_type"] == "ContinuityTransfer"
    assert data["status"] == "ACTIVE_TRUTH"
    assert data["admission_index_ref"] == "claim-classes/index.json"
    assert data["governing_law_version_ref"] == "law/versions/current/law-version-0001.json"
    assert data["governing_freeze_object_ref"] == "freeze/objects/current/freeze-object-0001.json"
    assert data["claim_class_ref"] == "claim-classes/continuity-transfer.json"
    assert data["historical_archive_ref"] == "continuity/objects/history/"
