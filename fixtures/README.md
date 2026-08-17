# fixtures/

| Carpeta | Regla | Contenido actual |
| --- | --- | --- |
| [`smoke/`](smoke/) | Debe validar contra su schema; usado para CI rápida | Un ejemplo por cada uno de los 10 contratos, más `action-result/action-result-002-rollback.json` (AC12) |
| [`validation/`](validation/) | Congelado — nunca se ajusta para hacer pasar una métrica | Secuencia security-event → incident → recommendation independiente de `smoke/` |
| [`negative/`](negative/) | Debe **fallar** la validación de schema | 3 casos (ver `negative/manifest.yaml`) |
| [`adversarial/`](adversarial/) | Schema-válido, pero debe bloquearse por política (F09) | 4 casos: prompt injection, tool poisoning, CVE falsa, fuera de allowlist (ver `adversarial/manifest.yaml`) |

Todo fixture declara procedencia implícita por su `run_id` y ruta; ninguno usa datos reales (`SECURITY.md`). El validador de `../validators/validate_fixtures.py` recorre las cuatro carpetas y aplica la regla que corresponde a cada una.

`smoke/action-result/action-result-002-rollback.json` (AC12, "rollback success = 1.00") no se escribió a mano: se generó invocando directamente `rollback.strategies.rollback_isolation` + `mark_rolled_back` de argos-cyber-tools (mismo código real que `argos-cyber-tools/tests/rollback/test_rollback_cycle.py` ejercita) contra `KubernetesExecutor.isolate_workload`, y luego se normalizaron solo `observed_at`/`started_at`/`ended_at`/`id`/`payload_hash` a los valores placeholder fijos que usa el resto de `smoke/` (2026-08-12, hashes `...0000`) — `status`, `changed_resources`, `verification` y `rollback_ref` son la salida real, sin editar.
