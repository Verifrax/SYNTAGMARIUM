from pathlib import Path

def test_required_schema_files_exist():
    required = [
        "schemas/object/repository.schema.json",
        "schemas/object/host.schema.json",
        "schemas/object/package.schema.json",
        "schemas/object/artifact.schema.json",
        "schemas/graph/world.schema.json",
        "schemas/epoch/epoch.schema.json",
        "schemas/projection/readme_contract.schema.json",
    ]
    for rel in required:
        assert Path(rel).exists(), rel
