from lab05 import *

## Extra Questions ##

# Q6
def filter(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    "*** YOUR CODE HERE ***"
    """
    for i in range(len(lst) - 1):
        if not pred(lst[i]):
            lst.pop(i)


    #Error occured when you have poped the first element in the list
    and then in for loop, i += 1 which will start with the first element in the new list.
    It will left behind with the second element.
    """

    #Going from the end of the list.If you have poped the false element,
    #you will at least check the former element with no left behind.

    i = len(lst) - 1
    while i >= 0:
        if not pred(lst[i]):
            lst.pop(i)
        i = i - 1


# Q7
def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    
    "*** YOUR CODE HERE ***"
    mid_element = len(lst) // 2
    last = len(lst) - 1

    for i in range(mid_element):
        lst[i], lst[last - i] = lst[last - i], lst[i]
    


# Q8
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split() # .split() returns a list of the words in the string. Try printing it!
    "*** YOUR CODE HERE ***"
    dic = {}
    for word in word_list:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

# Q9
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    m, n = 0, 1
    def fib():
        nonlocal m, n
        results = m
        m, n = n, m + n
        return results
    return fib
    
