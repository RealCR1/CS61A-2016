class Naturals():
	def __init__(self):
		self.current = 0

	def __next__(self):
		result = self.current
		self.current += 1
		return result

	def __iter__(self):
		return self


from operator import add
evens = IteratorCombiner(Naturals(), Naturals(), add)

class IteratorCombiner(object):
	def __init__(self, iterator1, iterator2, combiner):
		self.iter1 = iterator1
		self.iter2 = iterator2
		self.combiner = combiner
	def __next__(self):
		return self.combiner(next(self.iter1), next(self.iter2))



	def __iter__(self):
		return self
		

def perfect_squares():
	"""
	x = perfect_squares()
	>>>next(x)
	1
	>>>next(x)
	4
	"""
	current = 1
	while True:
		yield current ** 2
		current += 1

class Link:
	empty = ()
	def __init__(self, first, rest = empty):
		self.first = first
		self.rest = rest
	def __iter__(self):
		x = self
		while x != empty:
			yield x.first
			x = x.rest
			

