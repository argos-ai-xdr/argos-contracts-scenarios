# asyncapi/

Eventos sobre NATS JetStream (ADR-002). Cada mensaje referencia el schema de `../schemas/` correspondiente.

| Spec | Subjects |
| --- | --- |
| `asset-events.yaml` | `asset.snapshot.v1`, `vulnerability.finding.v1` |
| `security-events.yaml` | `security.event.v1`, `security.event.v1.dlq` |
| `incident-events.yaml` | `incident.v1` |

`Recommendation`, `PolicyDecision`, `Approval`, `ActionResult`, `EvidenceManifest` y `SOCHandover` no tienen spec AsyncAPI propia en esta primera versión: `Approval`/`Recommendation`/`EvidenceManifest` se exponen vía `../openapi/`; `PolicyDecision`/`ActionResult` viven internamente en `argos-cyber-tools` y se documentarán aquí si se confirma que necesitan un canal NATS propio (ARG-020/021).
