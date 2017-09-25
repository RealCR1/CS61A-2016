a = [1, 5, 4, [2, 3], 3]
print(a[0], a[-1])
len(a)

def tree(label, branches = []):
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_leaf(tree):
	return not branches(tree)

def square_tree(t):
	"""Return a tree with the square of every element in t."""
	if is_leaf(t):
		return tree(label(t) ** 2)
	else:
		return tree(label(t) ** 2, [square_tree(b) for b in branches])

def height(t):
	"""
	Return the height of the tree.
	"""
	if is_leaf(t):
		return 0
	else:
		return 1 + max([height(b) for b in branches(t)])



def tree_max(t):
	"""Return the max of the tree."""
	if is_leaf(t):
		return label(t)
	else:
		return max([label(t)] + [tree_max(b) for b in branches(t)])



