def multiply(m, n):
    """
    >>>multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return m + multiply(m, n-1)

def multiply_other(m, n):
    """
    Use the different way to resolve this problems
    """
    if m == 0:
        return 0
    elif m == 1:
        return m
    else:
        return n + multiply(m-1, n)

def countdown(n):
    """
    >>>countdown(3)
    3
    2
    1
    """
    assert n >= 1, 'You shoulf check your input, it should be positive integar.'
    if n == 1:
        return print("1")
    else:
        print(n)
        return countdown(n-1)

def sum_countdown(n):
    """
    >>>sum_countdown(3)
    6
    """
    sum, i = 0,1
    while i <= n:
        sum += i
        i += 1
    return sum

def sum_digits(n):
    if n % 10 == n:
        return n
    else:
        return n%10 + sum_digits(n//10)
