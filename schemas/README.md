# schemas/ — los 10 contratos v1 del documento maestro + 1 excepción (ADR-051/ADR-054)

Cada `<contrato>/v1.schema.json` compone `../../envelope/v1/argos-envelope.schema.json` vía `allOf` y añade sus campos específicos. Fuente: documento maestro v0.5, secciones 5.5 y 6.5, salvo donde se indica "DERIVADO" en la `description` del schema (campos no enumerados literalmente en el documento).

El conjunto de 10 sigue siendo cerrado por decisión explícita (documento maestro §6.5). `safety-envelope/` es la única excepción, autorizada contrato-por-contrato por ADR-051 (que la cita como ejemplo explícito) y ratificada por su propio ADR-054 — no reabre la decisión de los ~32 contratos nuevos del prompt maestro de arquitectura objetivo v0.6.25.x.

| Contrato | Fuente | Productor → consumidor |
| --- | --- | --- |
| [`security-event/`](security-event/v1.schema.json) | Literal (5.5 "Event") | Wazuh/Falco/Hubble/Audit → correlator |
| [`asset-snapshot/`](asset-snapshot/v1.schema.json) | Derivado (F01, AC02) | CMAM/NetBox/KAudit → risk-engine |
| [`vulnerability-finding/`](vulnerability-finding/v1.schema.json) | Derivado (F02/F03, gate 6.5) | Trivy/OpenVAS/VMT → risk-engine |
| [`incident/`](incident/v1.schema.json) | Literal (5.5) | correlator → LangGraph/SmartOps |
| [`recommendation/`](recommendation/v1.schema.json) | Literal (5.5) | LangGraph → OPA/SmartOps |
| [`policy-decision/`](policy-decision/v1.schema.json) | Literal (5.5) + ADR-005 | OPA → agent/SOAR |
| [`approval/`](approval/v1.schema.json) | Literal (5.5) | SmartOps → Shuffle |
| [`action-result/`](action-result/v1.schema.json) | Literal (5.5) | Shuffle/tool → SmartOps/evidence |
| [`evidence-manifest/`](evidence-manifest/v1.schema.json) | Literal (5.5 "Evidence") | evidence-writer → release gate |
| [`soc-handover/`](soc-handover/v1.schema.json) | Literal (5.5) | SOC adapter → SOC |
| [`safety-envelope/`](safety-envelope/v1.schema.json) | Prompt maestro v0.6.25.3 (SAFETY ENVELOPE) + ADR-054 | Safety Kernel → Independent Verifier/OPA (producido, aún no consumido — ver ADR-054) |

Los campos "DERIVADO" deben revisarse contra el schema real que publiquen ARG-004/007/008 — están marcados explícitamente para que nadie los trate como decisión ya ratificada.
