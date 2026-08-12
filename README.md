# argos-contracts-scenarios

Fuente autoritativa de los contratos de información, fixtures, escenarios y datos controlados usados por productores, consumidores y evaluadores de `argos-ai-xdr`. Ningún otro repositorio define su propio schema de `SecurityEvent`, `Incident`, etc. — todos importan de aquí.

Parte de la organización [`argos-ai-xdr`](https://github.com/argos-ai-xdr). Arquitectura autoritativa y ADR en [`argos-control`](https://github.com/argos-ai-xdr/argos-control).

## Contenido

| Carpeta | Contenido |
| --- | --- |
| `envelope/v1/` | ARGOS Event Envelope v1 (ADR-001): wrapper común a todo evento |
| `schemas/` | Los 10 contratos v1 (JSON Schema) |
| `openapi/` | APIs síncronas: incident, recommendation, approval, evidence |
| `asyncapi/` | Eventos asíncronos sobre NATS: asset, security, incident |
| `fixtures/` | `smoke/`, `validation/`, `negative/`, `adversarial/` — datos de prueba versionados |
| `scenarios/ARGOS-CYB-01/` | El escenario vertical reproducible (C-06/C-07/C-08) |
| `snapshots/` | Manifiestos de snapshots CTI/vulnerabilidades fijados por fecha y hash |
| `mappings/` | OCSF, ECS, ATT&CK, CVE/PURL |
| `generators/` | Scripts para regenerar snapshots/fixtures de forma reproducible |
| `validators/` | Validación de fixtures contra `schemas/` |
| `tests/` | `schema/`, `compatibility/`, `replay/` |

## Reglas de compatibilidad (ver ADR-001 y `argos-control/compatibility/contracts.yaml`)

* **PATCH**: corrige documentación o restricciones sin cambiar el payload.
* **MINOR**: añade campos opcionales — `additionalProperties: true` en cada schema es deliberado para no romper consumidores ante un MINOR.
* **MAJOR**: rompe compatibilidad; exige migrador, fixtures duales y actualización de `argos-control/compatibility/contracts.yaml`.
* IDs no reutilizables (UUID/ULID); timestamps UTC RFC 3339; hashes SHA-256.
* Prohibido: PII, secretos, tokens, prompts sensibles, chain-of-thought (ADR-016).

## Reglas comunes de la organización

* Rama principal: `main`. Sin rama permanente `develop`.
* Pull request obligatorio; revisión de `CODEOWNERS`; checks de CI obligatorios (incluye validación de schema y de compatibilidad — un cambio incompatible sin versión MAJOR se rechaza en CI).
* Prohibido push directo, force-push y borrado de `main`.
* Ningún dataset real, evidencia generada ni secreto en Git — solo fixtures pequeños y manifiestos de snapshots (hash, no contenido completo).

Ver `docs/development.md` para cómo trabajar en este repositorio.
