from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROLE_REQUIRED = {
    "role_id",
    "summary",
    "allowed_host_classes",
    "forbidden_adjacent_semantics",
    "required_readme_fields",
    "required_projection_features",
    "forbidden_claims",
}

class LawSurfaceTest(unittest.TestCase):
    def test_role_catalog_files_are_valid(self) -> None:
        role_files = sorted((ROOT / "roles").glob("*/role.json"))
        self.assertTrue(role_files, "no role.json files found")
        seen = set()
        for path in role_files:
            with self.subTest(path=str(path.relative_to(ROOT))):
                obj = json.loads(path.read_text(encoding="utf-8"))
                self.assertTrue(ROLE_REQUIRED.issubset(obj.keys()))
                self.assertEqual(obj["role_id"], path.parent.name)
                self.assertNotIn(obj["role_id"], seen)
                seen.add(obj["role_id"])

    def test_core_schemas_are_valid_json(self) -> None:
        schema_files = sorted((ROOT / "schemas").rglob("*.json"))
        self.assertTrue(schema_files, "no schema files found")
        for path in schema_files:
            with self.subTest(path=str(path.relative_to(ROOT))):
                obj = json.loads(path.read_text(encoding="utf-8"))
                self.assertIsInstance(obj, dict)

    def test_global_invariants_exist(self) -> None:
        names = {p.name for p in (ROOT / "invariants" / "global").glob("*.md")}
        required = {
            "one_active_truth.md",
            "projection_subordination.md",
            "historical_surfaces_self_identify.md",
            "one_host_one_owner_one_role.md",
            "one_package_one_source_repo.md",
            "one_repo_one_primary_role.md",
            "default_branch_main.md",
            "apache_2_license_permanence.md",
            "thirty_second_legibility.md",
        }
        self.assertTrue(required.issubset(names))

if __name__ == "__main__":
    unittest.main()
