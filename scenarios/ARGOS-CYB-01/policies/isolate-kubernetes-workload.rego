# F07 (documento maestro v0.5, 5.3): "ALLOW para dry-run; APPROVAL_REQUIRED
# para execute; DENY fuera de allowlist." Política de referencia para el
# escenario ARGOS-CYB-01 — la política real y firmada vive en
# argos-cyber-tools/policies/opa/; esta copia es un fixture de política
# usado por el harness de argos-validation para reproducir el escenario sin
# depender de ese repositorio.
#
# target_allowlist a granularidad de RECURSO concreto
# ("deployment/gseg-simulado"), no de namespace: una allowlist de namespace
# autorizaría implícitamente cualquier deployment de ese namespace, no solo
# el activo del escenario — mismo criterio que
# argos-cyber-tools/policies/opa/isolate_kubernetes_workload.rego, cuya
# propia nota señalaba esta copia como desactualizada (namespace en vez de
# recurso). Nadie carga este archivo en tiempo de ejecución (es solo
# referencia documental, ver ground-truth/fixtures-and-ground-truth.yaml),
# pero mantenerlo desalineado de la política real invita a copiar el valor
# equivocado en el futuro.
package argos.argos_cyb_01.isolate_kubernetes_workload

import future.keywords.if

default decision := {"result": "DENY", "reason": "no matching rule"}

target_allowlist := {"deployment/gseg-simulado"}

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
