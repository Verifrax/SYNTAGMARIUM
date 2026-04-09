import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class VerdictLawContractTest(unittest.TestCase):
    def test_verdict_schema_loads(self):
        payload = json.loads((ROOT / "schemas" / "object" / "verdict.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["title"], "VERIFRAX Verdict")
        self.assertIn("law_ref", payload["required"])

    def test_verdict_invariants_exist(self):
        self.assertTrue((ROOT / "invariants" / "global" / "no_verdict_without_pinned_law.yaml").exists())
        self.assertTrue((ROOT / "invariants" / "global" / "no_public_verdict_outranks_accepted_state.yaml").exists())

if __name__ == "__main__":
    unittest.main()
