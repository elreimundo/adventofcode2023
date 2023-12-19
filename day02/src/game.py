class Game:
	def __init__(self, id: int):
		self.id = id
		self.bag = {}

	def reveal(self, count: int, color: str):
		if color in self.bag:
			self.bag[color] = count if count > self.bag[color] else self.bag[color]
		else:
			self.bag[color] = count

	def could_have_resulted_from(self, other_game) -> bool:
		for color in self.bag:
			if color not in other_game.bag or self.bag[color] > other_game.bag[color]:
				return False
		return True

	def calculate_power(self):
		power = 1
		for color in self.bag:
			power *= self.bag[color]
		return power
