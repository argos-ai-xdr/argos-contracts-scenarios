# F07 (documento maestro v0.5, 5.3): "ALLOW para dry-run; APPROVAL_REQUIRED
# para execute; DENY fuera de allowlist." Política de referencia para el
# escenario ARGOS-CYB-01 — la política real y firmada vive en
# argos-cyber-tools/policies/opa/; esta copia es un fixture de política
# usado por el harness de argos-validation para reproducir el escenario sin
# depender de ese repositorio.
package argos.argos_cyb_01.isolate_kubernetes_workload

import future.keywords.if

default decision := {"result": "DENY", "reason": "no matching rule"}

target_allowlist := {"namespace/argos-cyber-range"}

decision := {"result": "ALLOW_DRY_RUN", "reason": "dry-run siempre permitido dentro del target allowlist"} if {
	input.action == "dry-run"
	input.target in target_allowlist
}

decision := {"result": "APPROVAL_REQUIRED", "reason": "execute requiere aprobación humana vinculada al action_id"} if {
	input.action == "execute"
	input.target in target_allowlist
	input.tool == "isolate_kubernetes_workload"
}

decision := {"result": "DENY", "reason": sprintf("target %v fuera de allowlist", [input.target])} if {
	not input.target in target_allowlist
}
