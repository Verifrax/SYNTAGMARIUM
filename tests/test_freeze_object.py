import json
from pathlib import Path

def test_current_freeze_object_exists_and_is_aligned():
    path = Path(freeze/objects/current/freeze-object-0001.json)
    assert path.is_file()
    data = json.loads(path.read_text())
    assert data[object_type] == FreezeObject
    assert data[freeze_object_id] == freeze-object-0001
    assert data[status] == ACTIVE_TRUTH
    assert data[governing_law_version_ref] == law/versions/current/law-version-0001.json
    assert data[admission_index_ref] == claim-classes/index.json
    chain = data[freezes_minimum_object_chain]
    assert freeze-object in chain
    assert continuity-transfer in chain
    assert data[historical_archive_ref] == freeze/objects/history/
