import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def test_kernel_indexes_and_current_law_are_machine_readable():
    law = load("law/versions/current/law-version-0001.json")
    roles = load("roles/index.json")
    schemas = load("schemas/index.json")
    invariants = load("invariants/index.json")
    transitions = load("transitions/index.json")
    contracts = load("contracts/index.json")

    assert law["surface_roots"]["roles_index"] == "roles/index.json"
    assert law["surface_roots"]["schemas_index"] == "schemas/index.json"
    assert law["surface_roots"]["contracts_index"] == "contracts/index.json"
    assert law["surface_roots"]["invariants_index"] == "invariants/index.json"
    assert law["surface_roots"]["transitions_index"] == "transitions/index.json"
    assert law["current_freeze_object_ref"] == "freeze/objects/current/freeze-object-0001.json"
    assert law["current_continuity_transfer_object_ref"] == "continuity/objects/current/continuity-transfer-0001.json"

    assert roles["object_type"] == "RoleCatalog"
    assert schemas["object_type"] == "SchemaCatalog"
    assert invariants["object_type"] == "InvariantCatalog"
    assert transitions["object_type"] == "TransitionCatalog"
    assert contracts["object_type"] == "ContractCatalog"

def test_transition_catalog_covers_four_kernel_paths():
    transitions = load("transitions/index.json")
    classes = {entry["transition_class"] for entry in transitions["entries"]}
    assert classes == {"LAWFUL", "REPAIRABLE", "QUARANTINED", "EXCEPTION"}
