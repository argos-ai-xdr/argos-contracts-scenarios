# envelope/

`v1/argos-envelope.schema.json` es el wrapper común (ADR-001). Los 10 contratos de `../schemas/` lo componen vía `allOf` y añaden sus campos específicos — no lo duplican.

`native_ref` es opcional a nivel de envelope porque no todos los contratos derivan de un evento de una fuente externa (p. ej. `Approval` lo emite SmartOps, no un sensor); cada schema de `../schemas/` decide si lo hace `required` para su caso.
