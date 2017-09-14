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
