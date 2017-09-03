
def mul_rational(x, y):
	return rational(numer(x) * numer(y), donom(x) * donom(y))

def equ_rational(x, y):
	return numer(x) * donom(y) == numer(y) * donom(x)

def add_rational(x, y):
	nx, dx = numer(x), donom(x)
	ny, dy = numer(x), donom(y)
	return rational(nx * dy + ny * dx, dx * dy)

def print_rational(x):
	print(numer(x), "/", donom(x))

#define the constructor and selector
def rational(n, d):
	return [n, d]

def numer(x):
	return x[0]

def donom(x):
    return x[1] 

"""
#In this way, we aren't need list data type at all
#we just need function,x is a function at there.
def rational(n, d):
	def select(name):
		if name == 'n':
			return n
	    elif name == 'd':
	    	return d
	return select

def numer(x):
	return x('n')

def donom(x):
	return x('d')

"""