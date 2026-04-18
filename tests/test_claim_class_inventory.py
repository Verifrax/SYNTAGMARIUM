from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CLAIM_DIR = ROOT / "claim-classes"

REQUIRED_IDS = {
    "law-version",
    "freeze-object",
    "accepted-epoch",
    "authority-object",
    "execution-receipt",
    "verification-result",
    "recognition-object",
    "recourse-object",
    "continuity-transfer",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_claim_class_index_is_complete():
    index = load(CLAIM_DIR / "index.json")
    assert index["object_type"] == "ClaimClassIndex"
    listed = {entry["claim_class_id"] for entry in index["classes"]}
    assert listed == REQUIRED_IDS
    assert [entry["chain_stage"] for entry in index["classes"]] == list(range(1, 10))


def test_each_claim_class_object_is_active_and_typed():
    for path in sorted(CLAIM_DIR.glob("*.json")):
        if path.name == "index.json":
            continue
        obj = load(path)
        assert obj["object_type"] == "ClaimClass"
        assert obj["status"] == "active"
        assert obj["governing_boundary"] == "SYNTAGMARIUM"
        assert "ACTIVE_TRUTH" in obj["truth_modes"]
        assert "HISTORICAL_SNAPSHOT" in obj["truth_modes"]
        assert obj["claim_class_id"] in REQUIRED_IDS
        assert obj["minimum_required_fields"]
        assert obj["admission_rules"]
        assert "canonical_object_family" in obj
