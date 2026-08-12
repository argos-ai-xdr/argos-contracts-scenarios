# Desarrollo en argos-contracts-scenarios

## Requisitos

* `git`, `make`, `python3` con `pyyaml` y `jsonschema`.

## Comandos

```bash
make bootstrap   # instala pre-commit y dependencias de validación
make validate    # cada schemas/*/v1.schema.json es JSON Schema válido (Draft 2020-12)
make test        # cada fixture de fixtures/{smoke,validation,negative,adversarial}
                  # valida (o falla, según corresponda) contra su schema
```

## Cómo añadir un contrato o campo nuevo

1. Si es un contrato nuevo: crear `schemas/<nombre>/v1.schema.json`, un ejemplo válido en `fixtures/smoke/<nombre>/` y uno inválido en `fixtures/negative/<nombre>/`.
2. Si es un campo opcional nuevo (MINOR) en un contrato existente: añadirlo a `properties`, nunca quitar `additionalProperties: true`, añadir un fixture en `fixtures/validation/` que lo use.
3. Si rompe compatibilidad (MAJOR): ver `CONTRIBUTING.md` — fixtures duales y coordinación con `argos-control/compatibility/contracts.yaml`.
4. Actualizar `openapi/` o `asyncapi/` si el contrato se expone por API o por evento.

## Antes de abrir un PR

1. `make validate` y `make test` sin errores.
2. El PR enlaza una historia `ARG-###`.
3. Ningún fixture nuevo contiene PII, secretos ni datos reales (ver `SECURITY.md`).
