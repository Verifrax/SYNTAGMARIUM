import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RoleRootTest(unittest.TestCase):
    def test_only_sovereign_roles_have_root_yaml(self):
        expected = {
            "roles/constitutional_law/root.yaml",
            "roles/reconciler/root.yaml",
            "roles/world_state/root.yaml",
        }
        actual = {
            str(p.relative_to(ROOT)).replace("\\\\", "/")
            for p in (ROOT / "roles").rglob("root.yaml")
        }
        self.assertEqual(actual, expected)

    def test_required_catalog_files_exist(self):
        expected = {
            "contracts/host_body/required_fields.yaml",
            "contracts/npm/package_contract.yaml",
            "contracts/readme/required_sections.yaml",
            "exceptions/policy.md",
            "exceptions/schema.json",
            "severities/hard_fail.yaml",
            "severities/quarantine.yaml",
            "severities/unknown.yaml",
            "severities/warn.yaml",
            "invariants/global/no_projection_outranks_law_or_epoch.yaml",
            "invariants/global/one_active_truth.yaml",
            "invariants/global/one_host_one_owner.yaml",
        }
        actual = {str(p.relative_to(ROOT)).replace("\\\\", "/") for p in ROOT.rglob("*") if p.is_file()}
        self.assertTrue(expected.issubset(actual))

if __name__ == "__main__":
    unittest.main()
