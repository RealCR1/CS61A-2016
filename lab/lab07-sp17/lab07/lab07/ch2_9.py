########################
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
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
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


###############
##Tree Class###
###############


class Tree:
    def __init__(self, entry, branches = ()):
        self.entry = entry
        for branch in branches:
            assert ininstance(branch, Tree):
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.entry, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.entry))

    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.entry + right.entry, (left, right))


def sum_entries(t):
    """
    Sum the entries of a Tree instance, which may be None.
    """
    return t.entry + sum([sum_entries(b) for b in t.branches])




