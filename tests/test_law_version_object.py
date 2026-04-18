import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_current_law_version_object_exists():
    p = ROOT / "law/versions/current/law-version-0001.json"
    assert p.is_file()

def test_current_law_version_object_shape():
    p = ROOT / "law/versions/current/law-version-0001.json"
    data = json.loads(p.read_text())
    assert data["object_type"] == "LawVersion"
    assert data["law_version_id"] == "law-version-0001"
    assert data["status"] == "ACTIVE_TRUTH"
    assert data["version"] == "0.1.0"
    assert data["admission_index_ref"] == "claim-classes/index.json"
    for key in [
        "constitution",
        "readme",
        "version_file",
        "claim_class_index",
        "roles_root",
        "schemas_root",
        "contracts_root",
        "invariants_root",
        "transitions_root",
    ]:
        assert key in data["effective_surface"]

def test_history_surface_exists():
    p = ROOT / "law/versions/history/README.md"
    assert p.is_file()
