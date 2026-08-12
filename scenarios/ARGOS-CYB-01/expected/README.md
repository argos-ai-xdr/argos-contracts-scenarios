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
