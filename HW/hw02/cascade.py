#This is an ordinary way to achieve this goal.
def cascade(n):
    """
    >>>cascade(123)
    ...123
    ...12
    ...1
    ...12
    ...123
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

#other implementation of cascade function
def cascade_other(n):
    print(n)
    if n >= 10:
        cascade_other(n//10)
        print(n)

#Inverse of cascade() function.
def cascade_inverse(n):
    """
    >>>cascade_inverse(1234)
    ...1
    ...12
    ...123
    ...1234
    ...123
    ...12
    ...1
    """

    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)