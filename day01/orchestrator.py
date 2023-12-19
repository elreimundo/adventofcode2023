from parser import parse, parse_with_literals
from calculator import calculate

from typing import List
from enum import Enum

class Strategy(Enum):
	SIMPLE = 0
	WITH_LITERALS = 1

def orchestrate(rows: List[str], strategy: Strategy = Strategy.SIMPLE) -> int:
	return calculate(
		parse(row) if strategy == Strategy.SIMPLE else parse_with_literals(row) for row in rows
	)
