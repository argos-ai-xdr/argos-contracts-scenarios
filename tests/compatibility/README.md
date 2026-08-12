# compatibility/

Pendiente de automatizar: comparar un schema modificado contra su versión anterior en Git y rechazar el PR si quita un campo `required`, cambia un `type` o pone `additionalProperties: false` donde antes era `true` sin que el PR declare explícitamente un bump MAJOR (ver `CONTRIBUTING.md` y `argos-control/compatibility/contracts.yaml`).

Hoy esta regla es un checklist manual de revisión de PR, no un script. Primer candidato a automatizar en ARG-006 (harness de `argos-validation`, que también consume estos schemas).
