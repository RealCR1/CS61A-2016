empty = 'empty'
def is_link(s):
    """ s is a linked list if it is empty or a (first, rest) pair.
    """
    return (len(s) == 2 and is_link(s[1])) or s == empty

def link(first, rest):
    """Construct a linked list from its first element and the rest.
    """
    assert is_link(rest), 'rest must be linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s.
    """
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of element of a linkeed list s.
    """
    assert is_link(s), 'rest only applies to linked list.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def len_link(s):
    """Return the length of linked list s.
    """
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_links(s, i):
    """Return the item which index is i in the linked list s.
    """
    while i > 0:
        s = rest(s)
        i -= 1
    return first(s)

"""These ways are using iteration to sovle the lenth and getitem.
Now we will try the recursion.
"""
def len_link_other(s):
    if s == empty:
        return 0
    return 1 + len_link_other(rest(s))

def getitem_links_other(s, i):
    if i == 0:
        return first(s)
    return getitem_links_other(rest(s), i-1)

def extend_link(s, t):
    assert is_link(s) and is_link(t), 'Please insert a listed link to combine.'
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def apply_all_link(f, s):
    """Apply f to each element of s.
    """
    assert is_link(s), 's should be a linked list'
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_all_link(f, rest(s)))


def keep_if_link(f, s):
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

def join_link(s, separator):
    """Return a string of all elements in s separated by separator.
    """
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
    

def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty)
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))
