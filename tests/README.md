# tests

* `schema/` — cada `schemas/**/v*.schema.json` es un JSON Schema Draft 2020-12 válido (`scripts/validate.sh`).
* `compatibility/` — un cambio a un schema existente no puede quitar un campo `required` ni cambiar su tipo sin bump de MAJOR (pendiente de automatizar; hoy es checklist manual en `CONTRIBUTING.md`).
* `replay/` — el escenario `scenarios/ARGOS-CYB-01/` puede reproducirse desde sus fixtures sin servicios externos (pendiente hasta que exista el harness real en `argos-validation`).

La validación fixture-contra-schema real vive en `../validators/validate_fixtures.py`, invocada por `scripts/test.sh` / `make test`.
