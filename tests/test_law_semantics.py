import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class LawSemanticsTest(unittest.TestCase):
    def test_constitution_names_sovereign_triplet(self):
        text = (ROOT / "CONSTITUTION.md").read_text(encoding="utf-8")
        self.assertIn("SYNTAGMARIUM", text)
        self.assertIn("ORBISTIUM", text)
        self.assertIn("CONSONORIUM", text)

    def test_readme_names_sovereign_triplet(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("SYNTAGMARIUM", text)
        self.assertIn("ORBISTIUM", text)
        self.assertIn("CONSONORIUM", text)

    def test_role_catalog_declares_expected_ids(self):
        expected = {
            "archive",
            "authority",
            "constitutional_law",
            "docs",
            "evidence_root",
            "governance",
            "intake",
            "proof_publication",
            "reconciler",
            "reference",
            "root",
            "runtime",
            "status",
            "tool",
            "verification",
            "world_state",
        }
        actual = set()
        for p in (ROOT / "roles").rglob("role.json"):
            data = json.loads(p.read_text(encoding="utf-8"))
            role_id = data.get("role_id") or data.get("id") or p.parent.name
            actual.add(role_id)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
