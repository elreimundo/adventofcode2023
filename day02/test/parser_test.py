from day02.src.parser import parse

def test_parse():
	game_1 = parse('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')

	assert(game_1.id == 1)
	assert(game_1.bag['blue'] == 6)
	assert(game_1.bag['red'] == 4)
	assert(game_1.bag['green'] == 2)
