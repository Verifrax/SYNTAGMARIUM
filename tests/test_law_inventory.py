import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class LawInventoryTest(unittest.TestCase):
    def test_required_top_level_surfaces_exist(self):
        expected_files = {"CONSTITUTION.md", "LICENSE", "README.md", "VERSION"}
        expected_dirs = {
            "contracts",
            "examples",
            "exceptions",
            "invariants",
            "roles",
            "schemas",
            "severities",
            "tests",
            "transitions",
        }
        actual_files = {p.name for p in ROOT.iterdir() if p.is_file()}
        actual_dirs = {p.name for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith(".")}
        self.assertTrue(expected_files.issubset(actual_files))
        self.assertTrue(expected_dirs.issubset(actual_dirs))

    def test_required_schema_files_exist(self):
        expected = {
            "schemas/epoch/epoch.schema.json",
            "schemas/graph/world.schema.json",
            "schemas/object/artifact.schema.json",
            "schemas/object/badge.schema.json",
            "schemas/object/evidence_surface.schema.json",
            "schemas/object/host.schema.json",
            "schemas/object/package.schema.json",
            "schemas/object/quarantine_record.schema.json",
            "schemas/object/repair_plan.schema.json",
            "schemas/object/repository.schema.json",
            "schemas/object/trust_summary.schema.json",
            "schemas/projection/artifact_entry.schema.json",
            "schemas/projection/host_entry.schema.json",
            "schemas/projection/package_entry.schema.json",
            "schemas/projection/readme_contract.schema.json",
            "schemas/projection/repo_entry.schema.json",
        }
        actual = {
            str(p.relative_to(ROOT)).replace("\\\\", "/")
            for p in (ROOT / "schemas").rglob("*.json")
        }
        self.assertEqual(actual, expected)

    def test_required_role_files_exist(self):
        expected = {
            "roles/archive/role.json",
            "roles/authority/role.json",
            "roles/constitutional_law/role.json",
            "roles/docs/role.json",
            "roles/evidence_root/role.json",
            "roles/governance/role.json",
            "roles/intake/role.json",
            "roles/proof_publication/role.json",
            "roles/reconciler/role.json",
            "roles/reference/role.json",
            "roles/root/role.json",
            "roles/runtime/role.json",
            "roles/status/role.json",
            "roles/tool/role.json",
            "roles/verification/role.json",
            "roles/world_state/role.json",
        }
        actual = {
            str(p.relative_to(ROOT)).replace("\\\\", "/")
            for p in (ROOT / "roles").rglob("role.json")
        }
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
