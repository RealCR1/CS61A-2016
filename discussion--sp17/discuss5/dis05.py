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
		if not lst[i] in list:
			list.append(lst[i])
	return list

	#mutation
    while el in lst:
    	lst.remove(el)
    lst[:] = [x for x in lst if x != el]

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


#Inheritance part
class Pet(object):
	def __init__(self, name, owner):
		self.is_alive = True
		self.name = name
		self.owner = owner
	def eat(self, thing):
		print(self.name + " ate a " + str(thing) + "!")
	def talk(self):
		print(self.name)

class Dog(Pet):
	"""dname, owner, coloring for Dog"""
	def __init__(self, name, owner, color):
		Pet.__init__(self, name, owner)
		self.color = color
	def talk(self):
		print(self.name + ' says woof!')


class Cat(Pet):
	def __init__(self, name, owner, lives = 9):
		Pet.__init__(self, name, owner)
		self.lives = lives
	def talk(self):
		print(self.name + ' says meow!')
	def lose_lives(self):
		if lives >= 2:
			lives -= 1
			retrun True
		elif lives = 1:
			retrun False

class NosiyCat(Cat):
	def __init__(self, name, owner, lives = 9):
		Cat.__init__(self, name, owner)
		self.lives = lives
	def talk(self):
		print(self.name + ' says meow!')



class Yolo(object):
	def __init__(self, metto):
		
		self.metto = metto
		
	def g(self):
		return self + metto






		



