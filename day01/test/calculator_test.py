from day01.calculator import calculate

def test_calculate():
	assert(calculate([1,2,3,4,5]) == 15)
	assert(calculate([6]) == 6)
	assert(calculate([]) == 0)