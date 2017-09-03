def count_partition(n, m):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	elif m < 0:
		return 0
	else:
		"""Use two different possibilities,
		one is including m which should analyze n-m
		And other part is use max size of m = m-1
		then reuse or recursion of count_partition()
		"""

		return count_partition(n-m, m) + count_partition(n, m-1)