from .parser import parse
from .game import Game

from typing import List

def orchestrate(game_to_care_about: Game, input: List[str]) -> int:
	total = 0
	for row in input:
		game = parse(row)
		if game.could_have_resulted_from(game_to_care_about):
			total += game.id
	return total
