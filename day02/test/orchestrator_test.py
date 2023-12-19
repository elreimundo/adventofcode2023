from day02.src.orchestrator import Orchestrator
from day02.src.game import Game

def test_orchestrate():
	target_game = Game(0)
	target_game.reveal(12, 'red')
	target_game.reveal(13, 'green')
	target_game.reveal(14, 'blue')

	orchestrator = Orchestrator("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines())

	assert(orchestrator.calculate_from_game(target_game) == 8)
	assert(orchestrator.calculate_total_power() == 2286)