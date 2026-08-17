# expected/

Mapa de cada checkpoint a la evidencia mínima esperada y, cuando existe, al fixture congelado que la representa (ver `../checkpoints/checkpoints.yaml` y `../../../fixtures/validation/`).

| CP | Evidencia mínima | Fixture congelado equivalente |
| --- | --- | --- |
| CP06 | `events.ndjson` | `fixtures/validation/security-event/wazuh-alert-frozen-001.json` |
| CP07 | `incident.json` | `fixtures/validation/incident/incident-frozen-001.json` |
| CP08 | `recommendation.json` | `fixtures/validation/recommendation/recommendation-frozen-001.json` |
| CP09-CP11 | `dry_run_result.json` / `action_result.json` | `fixtures/smoke/action-result/action-result-001.json` (aún no hay versión congelada en `validation/`) |
| CP10 | `approval.json` | `fixtures/smoke/approval/approval-001.json` (aún no hay versión congelada en `validation/`) |
| CP13 | `handover + manifest` | `fixtures/smoke/soc-handover/soc-handover-001.json`, `fixtures/smoke/evidence-manifest/evidence-manifest-001.json` |

CP00-CP05 no tienen fixture de contrato 1:1 todavía (`baseline_manifest.json`, `deployment_log`, `asset_diff.json`, `vulnerability_findings.json`, `risk_ranking.json`, `attack_path.json` — pendientes de ARG-007/008/009/011).

## sample-run/ (ARG-023: integración CP00-CP13 y trazabilidad end-to-end)

`sample-run/` ensambla, a partir de `fixtures/smoke/` (todos comparten
`run_id=run-smoke-001`), un run real con los 9 checkpoints respaldados por
uno de los 10 contratos v1 (CP02, CP03, CP06, CP07, CP08, CP09, CP10,
CP11, CP13 — CP09/CP11 reutilizan el mismo `action-result` de smoke para
dry-run y contención, como ya documentaba la tabla de arriba).

`argos-validation/harness/checkpoints.py` valida este directorio de
verdad: cada archivo contra su schema real y que TODOS comparten el mismo
`run_id` (trazabilidad end-to-end, no solo "cada pieza pasa su propio
test"). CP00, CP01, CP04, CP05 y CP12 (sin contrato v1 — artefactos
internos) se dejan deliberadamente SIN archivo: son un gap real y
conocido, no algo que este directorio deba fingir que ya existe.

```
cd argos-validation
python -m harness.checkpoints --run-dir ../argos-contracts-scenarios/scenarios/ARGOS-CYB-01/expected/sample-run
```
