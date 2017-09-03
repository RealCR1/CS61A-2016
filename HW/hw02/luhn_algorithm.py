def luhn_sum(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return luhn_sum_double(all_but_last) + last
def luhn_sum_double(n):
	all_but_last, last = split(n)
	luhn_digit = sum_digit(2 * last)
	if n < 10:
		return n
	else:
		return luhn_sum(all_but_last) + luhn_digit

def sum_digit(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return all_but_last + last

def split(n):
	return n//10, n %10
	