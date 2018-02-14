def eval_add(operands):
	cur = operands
	last = True
	while cur is not nil:
		last = calc_eval(cur.first) 
		if last is False:
			return False 
		cur = cur.second
	return last