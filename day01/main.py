import os

from orchestrator import orchestrate, Strategy

inputs = open(os.path.join(os.path.dirname(__file__), "calibration.my_data"), "r").readlines()

print(
	orchestrate(
		inputs
	)
)

print(
	orchestrate(
		inputs,
		Strategy.WITH_LITERALS
	)
)