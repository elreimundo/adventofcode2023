from typing import List

def calculate(ints: List[int]) -> int:
	running_total = 0
	for value in ints:
		running_total += value
	return running_total
