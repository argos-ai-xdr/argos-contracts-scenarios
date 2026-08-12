# Mapping MITRE ATT&CK

`incident` (`../../schemas/incident/v1.schema.json`) incluye técnicas ATT&CK (campo `attack_techniques`). Este directorio fija qué versión/snapshot de la matriz ATT&CK STIX 2.1 se usa (consistente con `../../snapshots/cti/`, ADR-007) para que un `technique_id` (p. ej. `T1078`) sea siempre resoluble contra la misma versión durante toda la ejecución de aceptación.

Pendiente (ARG-016): fijar versión de la matriz y el snapshot correspondiente.
