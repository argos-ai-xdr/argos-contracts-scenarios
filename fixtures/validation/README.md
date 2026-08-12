# validation/

Congelado — no se usa para ajustar prompts, reglas ni umbrales (regla del documento maestro v0.5, 5.3: "validation permanecerá congelado"). Cambiar un fixture de aquí requiere una historia `ARG-###` explícita y registrar el motivo en `CHANGELOG.md`, nunca un ajuste silencioso para hacer pasar una métrica.

Set inicial (ARG-006): una secuencia coherente e independiente de `fixtures/smoke/` — mismo tipo de incidente (escalada de privilegios en un workload de laboratorio) pero con IDs, timestamps y `run_id` propios, para que un evaluador no pueda confundir accidentalmente el fixture de humo con el de validación congelada.
