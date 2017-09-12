def tree(root, branches = []):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [root] + list(branches)

def root(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		branch_count = [count_leaves(b) for b in branches(tree)]
		return sum(branch_count)

def fib_tree(n):
	"""Construct trees by tree_recursive functions.
	Illustrate the tree_recursive functions to computate a Fibonacci number.
	"""
	if n == 0 or n == 1:
		return tree(n)
	else:
		left, right = fib_tree(n - 2), fib_tree(n - 1)
		fib_n = root(left) + root(right)
		return tree(fib_n, [left, right])

def partition_tree(n, m):
	"""Return a partition tree of n using parts of up to m."""
	if n == 0:
		return tree(True)
	elif n < 0 or m == 0:
		return tree(False)
	else:
		left = partition_tree(n-m, m)
		right = partition_tree(n, m-1)
		return tree(m, [left, right])

def partition_print(tree, partition = []):
	"""Construct each partitio as a list.
	When it reaches True leaf,the partition is printed.
	"""
	if is_leaf(tree):
		if root(tree):

			print(' + '.join(partition))
	else:
		left, right = branches(tree)
		m = str(root(tree))
		partition_print(left, partition + [m])
		partition_print(right, partition)

def print_tree()

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])