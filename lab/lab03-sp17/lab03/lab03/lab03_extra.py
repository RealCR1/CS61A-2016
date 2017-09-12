from lab03 import *

# Q6
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    return interleaved_helper(n, odd_term, even_term, 1)

def interleaved_helper(n, term0, term1, k):
    if k == n:
        return term0(k)
    return interleaved_helper(n, term1, term0, k+1) + term0(k)
#This is a solution from the reference book.
def interleaved_sum_other(n, odd_term, even_term):
    total, term0, term1 = interleaved_helper_other(n, odd_term, even_term)
    return total

def interleaved_helper_other(n, odd_term, even_term):
    if n == 1:
        return odd_term(1), even_term, odd_term
    else:
        total, term0, term1 = interleaved_helper_other(n-1, odd_term, even_term)
    return total + term0(n), term1, term0



# Q9
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10 + y * 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

# Q10
#Using the solution from the reference.
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
    
