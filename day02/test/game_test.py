from day02.src.game import Game

def test_game():
	game_1 = Game(1)
	game_2 = Game(2)
	game_1.reveal(1, 'red')
	assert(game_1.calculate_power() == 1)
	game_1.reveal(3, 'blue')
	assert(game_1.calculate_power() == 3)
	game_2.reveal(5, 'blue')
	game_2.reveal(5, 'green')
	assert(not game_1.could_have_resulted_from(game_2))
	assert(not game_2.could_have_resulted_from(game_1))
	game_2.reveal(5, 'red')
	assert(game_2.calculate_power() == 125)
	assert(game_1.could_have_resulted_from(game_2))
	assert(not game_2.could_have_resulted_from(game_1))
