from typing import List

def parse(input: str) -> int:
	start_position = 0
	end_position = -1
	while not input[start_position].isdigit():
		start_position += 1
	while not input[end_position].isdigit():
		end_position -= 1
	return int(input[start_position] + input[end_position])

LITERALS = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}

def parse_with_literals(input: str) -> int:
	start_position = 0
	first_digit = None
	end_position = -1
	last_digit = None
	while first_digit is None:
		if input[start_position].isdigit():
			first_digit = int(input[start_position])
		else:
			for key, value in LITERALS.items():
				if input[start_position:start_position + len(key)] == key:
					first_digit = value
		start_position += 1
	while last_digit is None:
		if input[end_position].isdigit():
			last_digit = int(input[end_position])
		else:
			for key, value in LITERALS.items():
				substring = input[end_position - len(key) + 1:] if end_position == -1 else input[end_position - len(key) + 1:end_position + 1]
				if substring == key:
					last_digit = value
		end_position -= 1
	return first_digit * 10 + last_digit


