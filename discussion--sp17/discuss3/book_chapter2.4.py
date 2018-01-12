from operator import add, sub
from operator import mul, truediv

#EXAMPLE ONE
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


#celsius temperature to fahrenhait
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




