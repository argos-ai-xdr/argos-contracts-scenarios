# Política de seguridad — argos-contracts-scenarios

Ver la política transversal en `argos-control/SECURITY.md`. Específico de este repositorio:

* `fixtures/adversarial/` contiene ejemplos de ataques (prompt injection, tool poisoning, CVE falsas, parámetros fuera de rango — F09) usados para probar que el sistema los **bloquea**. No son exploits reales ni contienen payloads funcionales contra sistemas externos; son datos estructurados que ejercitan la validación de schema y de política.
* `snapshots/` contiene únicamente manifiestos (hash, fecha, fuente) de snapshots CTI/vulnerabilidades — nunca el snapshot completo ni credenciales de acceso a la fuente.
* Ningún fixture contiene PII, secretos, tokens ni chain-of-thought (ADR-016). Un fixture que los necesite para ser realista se anonimiza antes de commitear.

## Reporte

Reportar vulnerabilidades o hallazgos vía el issue template `risk.yaml` o `exception.yaml` de `argos-control`, notificando al rol `qa-security-observer`.
