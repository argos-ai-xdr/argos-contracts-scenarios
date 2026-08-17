#!/usr/bin/env python3
"""Valida fixtures/ contra schemas/ y comprueba que cada carpeta cumple su regla:

  smoke/ y validation/   -> cada fixture DEBE validar
  negative/               -> cada fixture DEBE fallar (ver negative/manifest.yaml)
  adversarial/            -> cada fixture DEBE validar (bloqueo esperado es de
                              política, no de schema; ver adversarial/manifest.yaml)

Uso: python3 validators/validate_fixtures.py
"""
from __future__ import annotations

import json
import pathlib
import sys

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "schemas"
FIXTURES_DIR = ROOT / "fixtures"


def build_registry() -> Registry:
    resources = []
    for path in list(SCHEMAS_DIR.rglob("*.schema.json")) + [
        ROOT / "envelope/v1/argos-envelope.schema.json"
    ]:
        data = json.loads(path.read_text(encoding="utf-8"))
        resources.append((path.as_uri(), Resource.from_contents(data)))
    return Registry().with_resources(resources)


def validator_for(registry: Registry, contract: str) -> Draft202012Validator:
    schema_path = SCHEMAS_DIR / contract / "v1.schema.json"
    if not schema_path.exists():
        raise FileNotFoundError(f"No existe schemas/{contract}/v1.schema.json")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    schema = {**schema, "$id": schema_path.as_uri()}
    return Draft202012Validator(schema, registry=registry)


def check_should_validate(registry: Registry, fixture_path: pathlib.Path, contract: str) -> list[str]:
    v = validator_for(registry, contract)
    instance = json.loads(fixture_path.read_text(encoding="utf-8"))
    return [e.message for e in v.iter_errors(instance)]


def check_should_fail(registry: Registry, fixture_path: pathlib.Path, contract: str) -> list[str]:
    v = validator_for(registry, contract)
    instance = json.loads(fixture_path.read_text(encoding="utf-8"))
    errors = list(v.iter_errors(instance))
    return [] if errors else ["se esperaba que fallara la validación, pero validó sin errores"]


def main() -> int:
    registry = build_registry()
    failures: list[str] = []
    checked = 0

    # smoke/ y validation/: <categoria>/<contrato>/*.json debe validar.
    for category in ("smoke", "validation"):
        category_dir = FIXTURES_DIR / category
        if not category_dir.exists():
            continue
        for contract_dir in sorted(p for p in category_dir.iterdir() if p.is_dir()):
            contract = contract_dir.name
            for fixture_path in sorted(contract_dir.glob("*.json")):
                checked += 1
                errors = check_should_validate(registry, fixture_path, contract)
                if errors:
                    rel = fixture_path.relative_to(ROOT)
                    failures.append(f"{rel} debía validar contra {contract} pero falló: {errors}")

    # negative/: cada caso del manifest debe fallar.
    negative_manifest = FIXTURES_DIR / "negative" / "manifest.yaml"
    if negative_manifest.exists():
        cases = yaml.safe_load(negative_manifest.read_text(encoding="utf-8"))["cases"]
        for case in cases:
            checked += 1
            fixture_path = FIXTURES_DIR / "negative" / case["fixture"]
            errors = check_should_fail(registry, fixture_path, case["schema"])
            if errors:
                failures.append(f"negative/{case['fixture']}: {errors}")

    # adversarial/: cada caso del manifest debe validar contra schema
    # (expect_schema_valid) — el bloqueo esperado es semántico, no de schema.
    adversarial_manifest = FIXTURES_DIR / "adversarial" / "manifest.yaml"
    if adversarial_manifest.exists():
        cases = yaml.safe_load(adversarial_manifest.read_text(encoding="utf-8"))["cases"]
        for case in cases:
            checked += 1
            fixture_path = FIXTURES_DIR / "adversarial" / case["fixture"]
            if case.get("expect_schema_valid", True):
                errors = check_should_validate(registry, fixture_path, case["schema"])
            else:
                errors = check_should_fail(registry, fixture_path, case["schema"])
            if errors:
                failures.append(f"adversarial/{case['fixture']} ({case['id']}): {errors}")

    # checkpoints.yaml (ARG-023): evidence_files.contract, cuando no es
    # null, debe apuntar a uno de los 10 contratos v1 reales — evita que
    # este archivo se desincronice en silencio si un contrato se renombra.
    checkpoints_path = ROOT / "scenarios" / "ARGOS-CYB-01" / "checkpoints" / "checkpoints.yaml"
    if checkpoints_path.exists():
        known_contracts = {p.name for p in SCHEMAS_DIR.iterdir() if p.is_dir()}
        checkpoints = yaml.safe_load(checkpoints_path.read_text(encoding="utf-8")).get("checkpoints", [])
        checked += len(checkpoints)
        ids = [cp["id"] for cp in checkpoints]
        dupes = {i for i in ids if ids.count(i) > 1}
        if dupes:
            failures.append(f"checkpoints.yaml: id duplicado {sorted(dupes)}")
        for cp in checkpoints:
            for ev in cp.get("evidence_files", []):
                contract = ev.get("contract")
                if contract is not None and contract not in known_contracts:
                    failures.append(f"checkpoints.yaml: {cp['id']} referencia contract={contract!r}, no existe en schemas/")

    if failures:
        print(f"VALIDACIÓN DE FIXTURES FALLIDA ({len(failures)} de {checked}):")
        for f in failures:
            print(f"  - {f}")
        return 1

    print(f"validate_fixtures OK — {checked} fixtures verificados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
