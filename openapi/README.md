# openapi/

APIs síncronas. Cada operación referencia el schema de `../schemas/` correspondiente vía `$ref` — no se duplican los campos aquí.

| Spec | Cubre |
| --- | --- |
| `incident-api.yaml` | Consulta de `Incident` (solo lectura) |
| `recommendation-api.yaml` | Consulta de `Recommendation` (solo lectura) |
| `approval-api.yaml` | Registro y consulta de `Approval` (único POST de este repositorio: la decisión HITL) |
| `evidence-api.yaml` | Consulta de `EvidenceManifest` (solo lectura, sin acceso al contenido) |

Todas las URLs de `servers` son `TODO` — se fijan cuando `argos-platform` publique DNS real (DEP-02).
