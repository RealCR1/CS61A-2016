def count(s, value):
	"""Count the number of the sequence that equals to the special value.
	>>> count([1,2,3,4,1,2,3],3)
	2
	"""
	total, i = 0, 0
	while i < len(s):
		element = s[i]
		if element == value:
			total += 1
		i += 1
	return total

def count_other(s, value):
	total = 0
	for element in s :
		if element == value:
			total += 1
	return total

def divisors(n):
	return [1] + [ x for x in range(2,n+1) if n % x == 0]



numerals = {'I':1, 'V':5, 'X':10}