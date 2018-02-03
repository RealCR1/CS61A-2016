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




######################
##Fibnonacci Numbers##
######################
# A way to measure the efficency of this algorithm.


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

"""
Using tree-recursive function.
This way is so inefficient that fib(3) is duplicated.
"""
# A specific way to measure times of function call.

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

"""
Count the active frames which simultaneously active
during the course of computation.
"""

def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

#Memoization
"""
This way will store the last computation value 
decrease the computation which had been calculated.
"""

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

#fib function is actually only called once for each unique input for fib.


################################
##Make the Link class iterable##
################################

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
        """
        while self != empty:
            yield self.first
            self = self.rest
        """




#######################
##Recursive Objects#####
########################

class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first

        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)


def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

def link_expressions(s):
    """
    Return a string that would evaluate to s.
    """
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ',' + link_expressions(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)

def map_link(f, s):
    """
    Using function f to linked list s.
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    """
    Filtering the linked list in the condition of function f.
    """
    
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


def join_link(s, separator):
    if s is Link.empty:
        return ""

    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)


def partitions(n, m):
    """
    Return a linked list of partitions of n using parts of up
    to m. Each partition is represented as a linked list.
    """
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m-1)
        return with_m + without_m

def print_partitions(n, m):
    """
    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))











##################
##Chapter 1#######
##算法时间复杂度###
#################



def sqrt(x):
    y = 1.0
    while (y * y - x) > 1e-6:
        y = (y + x/y) / 2
    return y



    

def fib(n):
    """
    需要持续地递归，时间代价大概为 fib(n-1) + fib(n-2).
    所以，lim T = 1.618 ^ n, 所以当n趋向于无穷大时，T很大
    """

    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib(n):
    """
    由于循环前的工作只用做一次，所以总的工作量 为  n 的线性倍数。
    """
    f1 = f2 = 1
    for k in range(1, n):
        f1, f2 = f2, f1 + f2
    return f2


#计算两个模式相同（n*n)的矩阵(m1, m2)相乘的值,存入 (n*n)的矩阵m.
def matrix_mul(m1, m2):
    """
    计算其 复杂度时， 外面两侧循环分别为O(n),最内侧循环为(O(1) + O(n)*O(1) + O(1))化简得O(n)
    最终为O(n^3).
    """
    for i in range(n):
        for j in range(n):
            x = 0.0
            for k in range(n):
                x = x + m1[i][k] * m2[k][j]
            m[i][j] = x
    return m 


#求n阶矩阵的行列式的值
#方法一： 高斯消元法（将原来的矩阵(n*n)变成一个上三角矩阵，最后对于对角线的元素相乘得结果）

for i in range(n-1):
    """
    You can use the Numpy API, function 'tril' and 'triu'. 
    We will get lower triangle matrix and upper triangle matrix.
    """




##################
###Chapter 2######
##################


lass RationalPrevious:
    def __init__(self, num, den = 1):
        self.num = num
        self.den = den

    def plus(self, another):
        den = self.den * another.den
        num = self.num * another.den + self.den * another.num
        return Rational(num, den)

    def print(self):
        print(str(self.num)+"/"+str(self.den))


class Rational:
    @staticmethod
    def _gcd(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n%m, m
        return n

    def __init__(self, num, den = 1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gcd(num, den)
        self.num = sign * (num//g)
        self.den = den // g


    def __add__(self, another):
        den = self.den * another.den()
        num = (self.num * another.den() + self.den() * another.num())
        return Rational(num, den)

    def __mul__(self, another):
        return Rational(self.num * another.num(), self.den * another.den())

    def __floordiv__(self, another):
        if another.num() == 0:
            raise ZeroDivisionError
        return Rational(self.num * another.den(), self.den * another.num())


#######################
####Chapter 3##########
#######################

#Replacement in Linked list
class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __eq__(self, other):
        """
        Judge two linked list is equal or not.
        """
        p = self
        while p is not Link.empty and other is not Link.empty:
            if p.first != other.first:
                return False
            p, other = p.rest, othre.rest
        return p is Link.empty and other is Link.empty

