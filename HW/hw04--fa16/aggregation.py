from operator import min
def divisor(n):
	return  [x for x in range(1, n) if n%x == 0]

def width(area, height):
	assert area % height == 0
	return area // height

def perimeter(width, height):
	return 2 * width + 2 * height

def minimum_perimeter(area):
	heights = divisor(area)
	perimeters = [perimeter(width(area, h), h) for h in heights]
	return min(perimeters)