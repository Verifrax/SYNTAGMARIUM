#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

def need(cond, name):
    print(f"[VERIFY] {name}")
    if not cond:
        errors.append(name)

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

required_files = [
    "CONSTITUTION.md",
    "VERSION",
    "claim-classes/index.json",
    "law/versions/current/law-version-0001.json",
    "freeze/objects/current/freeze-object-0001.json",
    "continuity/objects/current/continuity-transfer-0001.json",
    "roles/index.json",
    "schemas/index.json",
    "invariants/index.json",
    "transitions/index.json",
    "contracts/index.json",
]

for rel in required_files:
    need((ROOT / rel).is_file(), f"file-present {rel}")

claim_index = load("claim-classes/index.json")
law = load("law/versions/current/law-version-0001.json")
roles = load("roles/index.json")
schemas = load("schemas/index.json")
invariants = load("invariants/index.json")
transitions = load("transitions/index.json")
contracts = load("contracts/index.json")

need(claim_index.get("object_type") == "ClaimClassIndex", "claim-index-type")
need(claim_index.get("status") == "ACTIVE_TRUTH", "claim-index-status")
need(claim_index.get("historical") is False, "claim-index-historical-false")

required_claims = {
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
present_claims = set()
for e in claim_index.get("entries", []):
    present_claims.add(e.get("claim_class_id") or e.get("id") or Path(e.get("path", "")).stem)
need(required_claims.issubset(present_claims), "claim-index-required-classes")

sr = law.get("surface_roots", {})
need(sr.get("claim_class_index") == "claim-classes/index.json", "law-claim-class-index")
need(sr.get("roles_index") == "roles/index.json", "law-roles-index")
need(sr.get("schemas_index") == "schemas/index.json", "law-schemas-index")
need(sr.get("contracts_index") == "contracts/index.json", "law-contracts-index")
need(sr.get("invariants_index") == "invariants/index.json", "law-invariants-index")
need(sr.get("transitions_index") == "transitions/index.json", "law-transitions-index")
need(law.get("current_freeze_object_ref") == "freeze/objects/current/freeze-object-0001.json", "law-freeze-ref")
need(law.get("current_continuity_transfer_object_ref") == "continuity/objects/current/continuity-transfer-0001.json", "law-continuity-ref")

need(roles.get("object_type") == "RoleCatalog", "roles-index-type")
need(roles.get("status") == "ACTIVE_TRUTH", "roles-index-status")
need(roles.get("historical") is False, "roles-index-historical-false")
need(len(roles.get("entries", [])) >= 5, "roles-index-nontrivial")

need(schemas.get("object_type") == "SchemaCatalog", "schemas-index-type")
need(schemas.get("status") == "ACTIVE_TRUTH", "schemas-index-status")
need(schemas.get("historical") is False, "schemas-index-historical-false")
need(len(schemas.get("entries", [])) >= 5, "schemas-index-nontrivial")

need(invariants.get("object_type") == "InvariantCatalog", "invariants-index-type")
need(invariants.get("status") == "ACTIVE_TRUTH", "invariants-index-status")
need(invariants.get("historical") is False, "invariants-index-historical-false")
need(len(invariants.get("entries", [])) >= 5, "invariants-index-nontrivial")

need(transitions.get("object_type") == "TransitionCatalog", "transitions-index-type")
need(transitions.get("status") == "ACTIVE_TRUTH", "transitions-index-status")
need(transitions.get("historical") is False, "transitions-index-historical-false")
transition_classes = {e.get("transition_class") for e in transitions.get("entries", [])}
need(transition_classes == {"LAWFUL", "REPAIRABLE", "QUARANTINED", "EXCEPTION"}, "transitions-index-complete")

need(contracts.get("object_type") == "ContractCatalog", "contracts-index-type")
need(contracts.get("status") == "ACTIVE_TRUTH", "contracts-index-status")
need(contracts.get("historical") is False, "contracts-index-historical-false")
need(len(contracts.get("entries", [])) >= 3, "contracts-index-nontrivial")

if errors:
    print("[FAIL] PHASE 4 / STEP 45 kernel object minimum verification failed")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

print("[PASS] PHASE 4 / STEP 45 kernel object minimum verified")
