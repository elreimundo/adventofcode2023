from .game import Game

def parse(input: str) -> Game:
	[game_string, reveal_string] = input.split(':')
	[_, game_number] = game_string.strip().split(' ')

	game = Game(int(game_number))

	for turn in reveal_string.strip().split(';'):
		for reveal in turn.strip().split(','):
			[count, color] = reveal.strip().split(' ')
			game.reveal(int(count), color)

	return game
