#Q2 in 1.1
def remove_all(el, lst):
	"""
	>>>x = [3, 1, 1, 2,3]
	>>>remove_all(1, x)
	>>>x
	[3, 1, 2]
	"""
	list = []
	for i in range(len(lst) - 1):
		if lst[i] in list:
			list.append(lst[i])
	return list

#Q3 in 1.1
def square_elements(lst):
    """
    >>>lst = [1, 2, 3]
    >>>square_elements(lst)
    >>>lst
    [1, 4, 9]
    """
    for i in range(len(lst) - 1):
    	lst[i] = lst[i] ** 2


   



