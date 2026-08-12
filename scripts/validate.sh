#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

python3 - <<'PY'
import json
import pathlib
import sys

import yaml
from jsonschema import Draft202012Validator

root = pathlib.Path(".")
errors = []

for path in root.rglob("*.y*ml"):
    if "/.git/" in str(path):
        continue
    try:
        list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    except yaml.YAMLError as exc:
        errors.append(f"{path}: YAML inválido: {exc}")

for path in root.rglob("*.json"):
    if "/.git/" in str(path):
        continue
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: JSON inválido: {exc}")

# Cada schemas/**/v*.schema.json debe ser, en sí mismo, un JSON Schema válido.
for path in (root / "schemas").rglob("*.schema.json"):
    schema = json.loads(path.read_text(encoding="utf-8"))
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # jsonschema.SchemaError
        errors.append(f"{path}: no es un JSON Schema Draft 2020-12 válido: {exc}")
    # additionalProperties puede declararse en el nivel superior o dentro de
    # cada rama de allOf (patrón usado por los 10 contratos: allOf[envelope, {..., additionalProperties: ...}]).
    branches = [schema] + schema.get("allOf", [])
    if not any("additionalProperties" in b for b in branches if isinstance(b, dict)):
        errors.append(f"{path}: additionalProperties debe decidirse explícitamente (regla de compatibilidad)")

required = {"name", "domain", "criticality", "owner", "backup_owner", "classification", "lifecycle"}
repo_yaml = root / "repository.yaml"
if not repo_yaml.exists():
    errors.append("repository.yaml no existe")
else:
    data = yaml.safe_load(repo_yaml.read_text(encoding="utf-8")) or {}
    missing = required - data.keys()
    if missing:
        errors.append(f"repository.yaml: faltan claves {sorted(missing)}")

if errors:
    print("VALIDACIÓN FALLIDA:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("validate OK")
PY
