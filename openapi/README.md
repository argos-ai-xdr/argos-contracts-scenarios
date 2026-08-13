# openapi/

APIs síncronas. `approval-api.yaml` referencia `../schemas/approval/v1.schema.json` vía `$ref` para la respuesta 201 (create_approval devuelve el envelope completo). Las demás describen inline la vista transformada real que sirve argos-smartops (`to_queue_item`/`to_incident_detail`/`to_recommendation_view`, y el objeto de metadatos de `api/evidence.py`) — no el schema del envelope completo, porque ninguno de esos endpoints lo devuelve tal cual (ver la `description` de cada spec). Mantener estos specs sincronizados con `argos-smartops/api/` cuando cambie una vista.

| Spec | Cubre |
| --- | --- |
| `incident-api.yaml` | Consulta de `Incident` (solo lectura) |
| `recommendation-api.yaml` | Consulta de `Recommendation` (solo lectura) |
| `approval-api.yaml` | Registro de `Approval` (único POST de este repositorio: la decisión HITL; sin endpoint de consulta todavía) |
| `evidence-api.yaml` | Consulta de `EvidenceManifest` (solo lectura, sin acceso al contenido) |

Todas las URLs de `servers` son `TODO` — se fijan cuando `argos-platform` publique DNS real (DEP-02).
