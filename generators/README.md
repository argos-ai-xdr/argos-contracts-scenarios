# generators/

Scripts para regenerar snapshots y fixtures de forma reproducible (hash estable, procedencia documentada). Ninguno implementado todavía: requieren decidir primero la fuente real de cada snapshot (ARG-005/ARG-016) y el destino de almacenamiento (Ceph RGW, `argos-platform/platform/ceph-rgw/`).

Previstos:

* `generate_cti_snapshot.py` — captura MISP + ATT&CK STIX 2.1, escribe el objeto en Ceph RGW y el manifiesto en `../snapshots/cti/`.
* `generate_vulnerability_snapshot.py` — captura CVE/NVD, CISA KEV, FIRST EPSS.
* `generate_smoke_fixtures.py` — regenera `../fixtures/smoke/` a partir de un run real anonimizado (no reemplaza los fixtures curados a mano mientras no exista un run real).

Ningún generador debe escribir directamente en `../fixtures/validation/` (congelado, ver `fixtures/validation/README.md`).
