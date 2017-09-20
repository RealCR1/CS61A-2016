def make_withdraw(balance):
	"""Return a withdraw function 
	that draws down balance with each call.
    """
	def withdraw(amount):
		nonlocal balance
		if amount > balance:
			return 'Insufficient funds'
		balance -= amount
		return balance
	return withdraw
wd = make_withdraw(100)
wd2 = make_withdraw(40)
wd(50)
wd(20)
"""
wd = make_withdraw(100)
wd2 = wd
This is wd2 function will change the value 
in the function wd.
"""

#Implementing lists and dictionaries
def mutable_link():
	contents = empty
	def dispatch(message, value = None):
		nonlocal contents
		if message == 'len':
			return len_link(contents)
		elif message == 'getitem':
			return getitem_link(contents, value)
		elif message == 'push_first':
			contents = link(value, contents)
		elif message == 'pop_first':
			f = first(contents)
			contents = rest(contents)
			return f
		elif message == 'str':
			return join_link(contents, ',')
	return dispatch

def to_mutable_link(source):
	s = mutable_link()
	for element in reversed(source):
		s('push_first', element)
	return s


#Implementation of dictionary.
def dictionary():
    records = []
    def getitem(key):
        matches = [r for r in range if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in range if r[0] != key]
        records = non_matches + [[key, value]]
    def dispatch(message, key = None, value = None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch

