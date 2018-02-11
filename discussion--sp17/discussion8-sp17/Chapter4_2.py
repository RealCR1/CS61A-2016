class LetterIter():
	"""docstring for LetterIter"""
	def __init__(self, start='a', end = 'e'):
		self.next_letter = start
		self.end = end
	def __next__(self):
		if self.next_letter == self.end:
			raise StopIteration
		letter = self.next_letter
		self.next_letter = chr(ord(letter)+1)
		return letter

class Letters:
	def __init__(self, start='a', end='e'):
		self.start = start
		self.end = end
	def __iter__(self):
		return LetterIter(self.start, self.end)




class Positives:
	def __init__(self):
		self.next_positive = 1
	def __next__(self):
		result = self.next_positive
		self.next_positive += 1
		return result

def double_and_print(x):
	print('***', x, '=>', 2*x, '***')
	return 2*x

counts = [1, 2 ,3]
for item in counts:
	print(item)


def all_paris(s):
	for item1 in s:
		for item2 in s:
			yield (item1, item2)


class Stream:
	"""
	A computed linked list.
	"""
	class empty:
		def __repr__(self):
			return 'Stream.empty'
	empty = empty()
	def __init__(self, first, compute_rest = lambda: empty):
		assert callable(compute_rest), 'compute_rest must be callable.'
		self.first = first
		self._compute_rest = compute_rest
	@property
	def rest(self):
		"""
		Return the rest of the stream, computing it if necessary.
		"""
		if self._compute_rest is not None:
			self._rest = self._compute_rest()
			self._compute_rest = None
		return self._rest
	def __repr__(self):
		return 'Stream({0}, <...>)'.format(repr(self.first))



