import os

from src.orchestrator import Orchestrator
from src.game import Game

inputs = open(os.path.join(os.path.dirname(__file__), "games.my_data"), "r").readlines()

target_game = Game(0)
target_game.reveal(12, 'red')
target_game.reveal(13, 'green')
target_game.reveal(14, 'blue')


orchestrator = Orchestrator(inputs)

print(
	orchestrator.calculate_from_game(target_game)
)

print(orchestrator.calculate_total_power())