#Use recursive way to solve the is_prime() function.
def is_prime(n):
	def helper(i):
		if i == n:
			return True
		elif n % i == 0:
			return False
		else:
			return helper(i + 1)
	return helper(2)



#Palindrome numbers
def is_palindroem(n):
	x, y = n, 0
	f = lambda: y * 10 + x % 10
	while x > 10:
		x, y = x // 10, f()
	return y == n

#
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count_digit(n//10, 10 - n%10)

def count_digit(n, digit):
    if n == 0:
        return 0
    else:
        if n%10 == digit:
            return count_digit(n//10, digit) + 1
        else:
            return count_digit(n//10, digit)


#Higher order function example
def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
a = cake()
"""When you call cake() function, it turns out to 'def cake()',
and then jump to 'return pie' which means to return to function pie(),
the outcome is 
sweets
cake
"""



#This is a long circle question, I have troubled in the last question.
#TypeError, function 'sub_rat(x, y)' return a tuple type which couldn't compared with 'int' type.
#Just use the same type data, I didn't think about it in the first time.
def cons(left, right):
    return (left, right)

def left(pair):
    return pair[0]

def right(pair):
    return pair[1]

from fractions import gcd

def make_rat(n, d):
    """The rational number n/d, assuming n, d are integers, d!=0"""
    g = gcd(n, d) if d > 0 else -gcd(n, d)
    n //= g; d //= g
    return cons(n, d)

def numer(r):
    """The numerator of rational number r."""
    return left(r)

def denom(r):
    """The denominator of rational number r."""
    return right(r)

def add_rat(x, y):
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x),
                    denom(x) * denom(y))

def mul_rat(x, y):
    """The product of rational numbers x and y."""
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))

def div_rat(x, y):
    """The quotient of rationals x/y.
    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> numer(c)
    9
    >>> denom(c)
    20
    """
    return make_rat(numer(x) * denom(y), denom(x) * numer(y))

def lt_rat(x, y):
    """Returns True if x < y as rational numbers; else False.
    >>> a, b = make_rat(6, 7), make_rat(12, 16)
    >>> lt_rat(a, b)
    False
    >>> lt_rat(b, a)
    True
    >>> lt_rat(a, b)
    False
    >>> a, b = make_rat(-6, 7), make_rat(-12, 16)
    >>> lt_rat(a, b)
    True
    >>> lt_rat(b, a)
    False
    >>> lt_rat(a, a)
    False
    """
    #Idea come from others.Oops
    first = numer(x) * denom(y)
    last = numer(y) * denom(x)
    return first < last
    """
    #It is wrong solution that typeError, tuple type and int type.
    if sub_rat(x, y) < 0:
        return True
    else:
        return False

def sub_rat(x, y):
    return make_rat(numer(x) * denom(y) - numer(y) * denom(x), denom(x) * denom(y))
"""


#Solution of calculation of Celsius degree and Fahrenhait degree in spite of the constraints.
from operator import add, sub
from operator import mul, truediv

def adder(a, b, c):
    return make_ternary_constraint(a, b, c, add, sub, sub)


def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)


def constant(connector, value):
    """The constraint that connect = value."""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint


def connector(name = None):
    """A connector between constraints."""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('conditionction detected')
                print('Contradiction detected:', val, 'vs', value)
    
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    
    return connector
    



def inform_all_except(source, message, constraints):
    """Inform all constraints of the message, except source."""
    for c in constraints:
        if c != source:
            c[message]()



def make_ternary_constraint(a, b, c, ab, ca, cb):
    """
    the constraint that ab(a, b) = c and ca(c, a) = b and cb(c, b) = a.
    """
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint


celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')


def converter(c, f):
    """
    Connect c to f with constraints to convert from Celsius to Fahrenheit.
    """
    u, v, x, y, w = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)



#Choose which to print
def cake():
    print('beets')
    def pie():
        print('candy')
        return 'cake'
    return pie

a = cake()

"""
Program is executing as follow, call function cake() --> that begins to execute the suite of the
body of the cake() function.So 'beets' is printed, but with return None.Then go to the return line.
calling the pie() function.And then, 'candy' is also printed and with return 'cake'.
so the assignment line 'a = cake()' is executed. Python terminal print the 'beets' but a is assigned
to 'cake'.
"""