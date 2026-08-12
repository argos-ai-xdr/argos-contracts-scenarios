# snapshots/

Manifiestos (fecha, hash, fuente, licencia) de los snapshots CTI y de vulnerabilidades fijados — nunca el snapshot completo ni consultas online en tiempo de ejecución (ADR-007, regla "reproducibilidad offline": "imágenes, modelos, políticas, datasets, CTI, schemas y runbooks quedan fijados por versión, digest y hash antes de aceptación").

| Carpeta | Contenido |
| --- | --- |
| `cti/` | Manifiestos de snapshots MISP y ATT&CK STIX 2.1 |
| `vulnerability-db/` | Manifiestos de snapshots CVE/NVD, CISA KEV y FIRST EPSS |
| `manifests/` | Manifiesto agregado por release (qué snapshot de cada fuente se usó en qué `release-manifest.yaml` de `argos-control`) |

Ninguna carpeta contiene todavía un snapshot real — se generan con `../generators/` a partir de ARG-005/ARG-016. El contenido completo del snapshot vive en Ceph RGW (ADR-006), no en Git.
