# Contribuir a argos-contracts-scenarios

1. Toda historia debe existir como issue `ARG-###` (ver `argos-control/project/backlog/backlog.yaml`). Primeras historias: ARG-004 (publicar envelope y contratos Asset/Vulnerability/SecurityEvent), ARG-005 (pipeline F01-F09, snapshots, hashes y data manifest).
2. Rama de trabajo: `feat/ARG-###-descripcion-corta`, `fix/...`.
3. Pull request obligatorio contra `main`. Sin push directo, force-push ni borrado de `main`.
4. Cambiar un schema de `schemas/`:
   - **PATCH/MINOR**: no requiere migrador; MINOR debe mantener `additionalProperties: true` y solo añadir campos opcionales.
   - **MAJOR**: requiere un fixture dual (`fixtures/validation/<contrato>/v1/` y `v2/`), actualizar `argos-control/compatibility/contracts.yaml`, y que los repos consumidores confirmen que probarán ambas versiones.
5. Todo fixture nuevo declara procedencia y hash (ver `fixtures/README.md`).
6. No incluir secretos, PII, datasets reales completos ni evidencia real (ADR-016) — solo fixtures pequeños y manifiestos.
7. `make validate` (valida schema de los schemas) y `make test` (valida cada fixture contra su schema) deben pasar antes de abrir el PR.
