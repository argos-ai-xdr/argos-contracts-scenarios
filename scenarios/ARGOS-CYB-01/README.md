# ARGOS-CYB-01

Escenario vertical reproducible que atraviesa C-06, C-07 y C-08 (documento maestro v0.5, sección 5). No depende de IBM X-Force ni de servicios propietarios.

| Archivo | Contenido |
| --- | --- |
| [`scenario.yaml`](scenario.yaml) | Ficha (5.1) e hipótesis/precondiciones/límites (5.2) |
| [`checkpoints/checkpoints.yaml`](checkpoints/checkpoints.yaml) | CP00-CP13 (5.4) |
| [`ground-truth/fixtures-and-ground-truth.yaml`](ground-truth/fixtures-and-ground-truth.yaml) | F01-F09 (5.3) |
| [`expected/`](expected/) | Mapa CP → fixture congelado |
| [`policies/`](policies/) | Política OPA de referencia (F07) |

Ejecutado sobre el cyber-range de `argos-platform` (namespace `argos-cyber-range`, allowlist en `cyber-range/targets/allowlist.yaml` de ese repo). Evaluado por `argos-validation` contra `argos-control/project/acceptance/acceptance-criteria.yaml` (AC01-AC14).
