# Arquitectura de argos-contracts-scenarios

Este repositorio es la fuente contract-first (`argos-control/architecture/logical/planos.md`, principio "Contract-first") consumida por todos los planos P2-P6: ningún componente comparte tablas internas con otro dominio, solo estos contratos versionados.

## Relación con el flujo end-to-end

Ver `argos-control/architecture/data-flows/end-to-end-flow.md`. Cada paso de ese flujo produce/consume uno de los 10 contratos de `schemas/`:

| Paso del flujo | Contrato |
| --- | --- |
| Sensores → normalizer | `security-event` (envelope v1, ADR-001) |
| Adaptadores de activos/vulnerabilidades | `asset-snapshot`, `vulnerability-finding` |
| Correlador → LangGraph/SmartOps | `incident` |
| LangGraph → OPA/SmartOps | `recommendation` |
| OPA → agent/SOAR | `policy-decision` |
| SmartOps → Shuffle | `approval` |
| Shuffle/tool → SmartOps/evidence | `action-result` |
| evidence-writer → release gate | `evidence-manifest` |
| SOC adapter → SOC | `soc-handover` |

## ARGOS-CYB-01

`scenarios/ARGOS-CYB-01/` es la instancia concreta de este flujo usada para la aceptación (S8, gate G7): sus checkpoints CP00-CP13 son, en la práctica, una ejecución completa de la tabla anterior con ground truth conocido.
