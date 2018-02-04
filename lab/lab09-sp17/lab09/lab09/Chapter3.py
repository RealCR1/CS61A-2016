###########################
##Interpreting Programs####
###########################

from ucb import main, trace, interact
from scheme_tokens import tokenize_lines, DELIMITERS
from buffer import Buffer, InputReader

# Pairs and Scheme lists

####################
##Expression Trees##
####################

class Pair(object):
    """A pair has two instance attributes: first and second.  For a Pair to be
    a well-formed list, second is either a well-formed list or nil.  Some
    methods only apply to well-formed lists.

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        if second is not nil:
            s += " . " + str(second)
        return s + ")"

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("ill-formed list")

class nil(object):
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):
        return self

nil = nil() # Assignment hides the nil class; there is only one instance


# Scheme list parser, without quotation or dotted lists.

def scheme_read(src):
    """Read the next expression from src, a Buffer of tokens.

    >>> lines = ['(+ 1 ', '(+ 23 4)) (']
    >>> src = Buffer(tokenize_lines(lines))
    >>> print(scheme_read(src))
    (+ 1 (+ 23 4))
    """
    if src.current() is None:
        raise EOFError
    val = src.pop()
    if val == 'nil':
        return nil
    elif val not in DELIMITERS:  # ( ) ' .
        return val
    elif val == "(":
        return read_tail(src)
    else:
        raise SyntaxError("unexpected token: {0}".format(val))

def read_tail(src):
    """Return the remainder of a list in src, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
    Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
    """
    if src.current() is None:
        raise SyntaxError("unexpected end of file")
    if src.current() == ")":
        src.pop()
        return nil
    first = scheme_read(src)
    rest = read_tail(src)
    return Pair(first, rest)


# Interactive loop

def buffer_input():
    return Buffer(tokenize_lines(InputReader('> ')))

@main
def read_print_loop():
    """Run a read-print loop for Scheme expressions."""
    while True:
        try:
            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
                print(repr(expression))
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            return

s = Pair(1, Pair(2, nil))
print(s)
print(s.map(lambda x: x+4))
expr = Pair('+', Pair(Pair('*', Pair(3, Pair(4, nil))), Pair(5, nil)))




########################
##Parsing Expressions###
########################

# Part I -- Lexical Analyzer
"""The scheme_tokens module provides functions tokenize_line and tokenize_lines
for converting (iterators producing) strings into (iterators producing) lists
of tokens.  A token may be:

  * A number (represented as an int or float)
  * A boolean (represented as a bool)
  * A symbol (represented as a string)
  * A delimiter, including parentheses, dots, and single quotes
"""

import string
import sys

_SYMBOL_STARTS = set('!$%&*/:<=>?@^_~') | set(string.ascii_lowercase)
_SYMBOL_INNERS = _SYMBOL_STARTS | set(string.digits) | set('+-.')
_NUMERAL_STARTS = set(string.digits) | set('+-.')
_WHITESPACE = set(' \t\n\r')
_SINGLE_CHAR_TOKENS = set("()'")
_TOKEN_END = _WHITESPACE | _SINGLE_CHAR_TOKENS
DELIMITERS = _SINGLE_CHAR_TOKENS | {'.'}

def valid_symbol(s):
    """Returns whether s is not a well-formed value."""
    if len(s) == 0 or s[0] not in _SYMBOL_STARTS:
        return False
    for c in s[1:]:
        if c not in _SYMBOL_INNERS:
            return False
    return True

def next_candidate_token(line, k):
    """A tuple (tok, k'), where tok is the next substring of line at or
    after position k that could be a token (assuming it passes a validity
    check), and k' is the position in line following that token.  Returns
    (None, len(line)) when there are no more tokens."""
    while k < len(line):
        c = line[k]
        if c == ';':
            return None, len(line)
        elif c in _WHITESPACE:
            k += 1
        elif c in _SINGLE_CHAR_TOKENS:
            return c, k+1
        elif c == '#':  # Boolean values #t and #f
            return line[k:k+2], min(k+2, len(line))
        else:
            j = k
            while j < len(line) and line[j] not in _TOKEN_END:
                j += 1
            return line[k:j], min(j, len(line))
    return None, len(line)

def tokenize_line(line):
    """The list of Scheme tokens on line.  Excludes comments and whitespace."""
    result = []
    text, i = next_candidate_token(line, 0)
    while text is not None:
        if text in DELIMITERS:
            result.append(text)
        elif text == '+' or text == '-':
            result.append(text)
        elif text == '#t' or text.lower() == 'true':
            result.append(True)
        elif text == '#f' or text.lower() == 'false':
            result.append(False)
        elif text == 'nil':
            result.append(text)
        elif text[0] in _NUMERAL_STARTS:
            try:
                result.append(int(text))
            except ValueError:
                try:
                    result.append(float(text))
                except ValueError:
                    raise ValueError("invalid numeral: {0}".format(text))
        elif text[0] in _SYMBOL_STARTS and valid_symbol(text):
            result.append(text)
        else:
            print("warning: invalid token: {0}".format(text), file=sys.stderr)
            print("    ", line, file=sys.stderr)
            print(" " * (i+3), "^", file=sys.stderr)

        text, i = next_candidate_token(line, i)
    return result

def tokenize_lines(input):
    """An iterator that returns lists of tokens, one for each line of the
    iterable input sequence."""
    return map(tokenize_line, input)
    	return iterative Lines



def calc_eval(exp):
	"""
	Evaluate a Calculator expression.
	"""
	if type(exp) in (int, float):
		return simplify(exp)
	elif isinstance(exp, Pair):
		arguments = exp.second.map(calc_eval)
		return simplify(calc_apply(exp.first, arguments))

	else:
		raise TypeError(exp + ' is not a number or call expression')


def calc_apply(operator, args):
	"""
	Apply the named operator to a list of args.
	"""
	if not isinstance(operator, str):
		raise TypeError(str(operator) + ' is not a symbol')
	if operator == '+':
		return reduce(add, args, 0)
	elif operator == '-':
		if len(args) == 0:
			raise TypeError(operator + ' requires at least 1 argument')
		elif len(args) == 1:
			return -args.first
            else:
                return reduce(sub, args.second, args.first)
        elif operator == '*':
            return reduce(mul, args, 1)
        elif operator == '/':
            if len(args) == 0:
                raise TypeError(operator + ' requires at least 1 argument')
            elif len(args) == 1:
                return 1/args.first
            else:
                return reduce(truediv, args.second, args.first)
        else:
            raise TypeError(operator + ' is an unknown operator')



