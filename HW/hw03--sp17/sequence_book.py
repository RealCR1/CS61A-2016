def right_binarize(tree):
	"""Construct a right_hand binary tree.
	"""
	if is_leaf(tree):
		return tree
	elif len(tree) > 2:
		tree = [tree[0], tree[1:]]
	return [right_binarize(b) for b in tree]
	
def is_leaf(tree):
	if len(tree) == 1:
		return True
	else:
		return False