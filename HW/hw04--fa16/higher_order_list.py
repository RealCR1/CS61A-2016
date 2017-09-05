from operator import add, mul
def reduce(reduce_fn, s , initial):
	reduced = initial
	for x in s:
		reduced = reduce_fn(reduced, x)
	return reduced

def keep_if(filter_fn, s):
	return [x for x in s if filter_fn(x)]

def divisor_of(n):
	divides_n = lambda x: n % x == 0
	return [1] + keep_if(divides_n, range(2, n))