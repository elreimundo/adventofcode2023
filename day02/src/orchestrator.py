from .parser import parse
from .game import Game

from typing import List

class Orchestrator:
	def __init__(self, input: List[str]):
		self.games = [parse(row) for row in input]

	def calculate_from_game(self, game_to_care_about: Game) -> int:
		total = 0
		for game in self.games:
			if game.could_have_resulted_from(game_to_care_about):
				total += game.id
		return total

	def calculate_total_power(self) -> int:
		total = 0
		for game in self.games:
			total += game.calculate_power()
		return total