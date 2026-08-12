# fixtures/

| Carpeta | Regla | Contenido actual |
| --- | --- | --- |
| [`smoke/`](smoke/) | Debe validar contra su schema; usado para CI rápida | Un ejemplo por cada uno de los 10 contratos |
| [`validation/`](validation/) | Congelado — nunca se ajusta para hacer pasar una métrica | Secuencia security-event → incident → recommendation independiente de `smoke/` |
| [`negative/`](negative/) | Debe **fallar** la validación de schema | 3 casos (ver `negative/manifest.yaml`) |
| [`adversarial/`](adversarial/) | Schema-válido, pero debe bloquearse por política (F09) | 4 casos: prompt injection, tool poisoning, CVE falsa, fuera de allowlist (ver `adversarial/manifest.yaml`) |

Todo fixture declara procedencia implícita por su `run_id` y ruta; ninguno usa datos reales (`SECURITY.md`). El validador de `../validators/validate_fixtures.py` recorre las cuatro carpetas y aplica la regla que corresponde a cada una.
