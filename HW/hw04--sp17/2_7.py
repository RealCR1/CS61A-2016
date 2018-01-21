def make_adder(n):
	def adder(k):
		return n + k
	return adder

add_three = make_adder(4)
results = add_three(3)

class Adder(object):
	def __init__(self, n):
		self.n = n

	def __call__(self, k):
		return self.n + k

add_three1 = Adder(4)
add_three(3)


class Number:
	def __add__(self, other):
		return self.add(other)
	def __mul__(self, other):
		return self.mul(other)


class Complex(Number):
	def add(self, other):
		return ComplexRI(self.real + other.real, self.imag + other.imag)
	def mul(self, other):
		magnitude = self.magnitude * other.magnitude
		return ComplexMA(magnitude, self.angle + other.angle)

		return ComplexMA(self.)

#Property

"""
Four attributes can be accessed without any call expressions
any change for 'real' or 'imag' will affect 'magnitude' and 'angle'.
"""

from math import atan2
class ComplexRI(Complex):
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag
		
		@property
		def magnitude(self):
			return (self.real ** 2 + self.imag ** 2) ** 0.5
		
		@property
		def angle(self):
			return atan2(self.imag, self.real)

		@property
		def __repr__(self):
			return 'ComplexRI({0:g},{1:g})'.format(self.real, self.imag)


"""
Four attributes can be accessed without any call expressions
any change for 'magnitude' and 'angle' will affect 'real' and 'imag'.
"""

from math import cos, sin, pi
class ComplexMA(Complex):
	def __init__(self, magnitude, angle):
		self.magnitude = magnitude
		self.angle = angle

	@property
	def real(self):
		return self.magnitude * cos(self.angle)

	@property
	def imag(self):
		return self.magnitude * sin(self.angle)

	@property
	def __repr__(self):
		return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)