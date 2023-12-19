from day01.src.orchestrator import orchestrate, Strategy

def test_orchestrate():
	assert(
		orchestrate("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()) == 142
	)
	assert(
		orchestrate(
			"""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines(),
			Strategy.WITH_LITERALS
		) == 281
	)