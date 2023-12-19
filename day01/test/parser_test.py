from day01.parser import parse, parse_with_literals

def test_parse():
	assert(parse("15") == 15)
	assert(parse("12345") == 15)
	assert(parse("1blarg2") == 12)
	assert(parse("a1b2c3d4e5fgh") == 15)

def test_parse_with_literals():
	assert(parse_with_literals("15") == 15)
	assert(parse_with_literals("a1b2c3d4e5fgh") == 15)
	assert(parse_with_literals("oneoneight") == 18)