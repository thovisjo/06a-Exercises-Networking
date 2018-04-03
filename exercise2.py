#!/usr/bin/python
'''

For each function, add three (doctest) unit tests. Each test should pass. The python script is currently configured to run those tests, so you can see the results by running the program

I have done the first one for you as an example. IDLE may be a useful way to see the expected output

'''
def multiply(a, b):
	"""
	>>> multiply(4, 3)
	12
	>>> multiply('a', 3)
	'aaa'
	>>> multiply((0,1),4)
	(0, 1, 0, 1, 0, 1, 0, 1)
	"""
	return a * b


def divide(a, b):
	"""
	
	
	
	"""
	try:
		return float(a) / float(b)
	except ValueError:
		return "You can't divide that data type!"
	except ZeroDivisionError:
		return "You can't divide by zero!"


def check_proximity(xy1, xy2):
	"""
	
	
	
	
	"""
	if type(xy1) is not tuple or type(xy2) is not tuple: return False
	if len(xy1) != 2 or len(xy2) != 2: return False
	if xy1 == xy2: return False
	if (abs(xy1[0] - xy2[0]) <= 1 and xy1[1] == xy2[1]) or (abs(xy1[1] - xy2[1]) <= 1 and xy1[0] == xy2[0]):
		return True
	return False



def update(x,y,dx,dy,gravity,air_resistance,WIDTH,HEIGHT):
	"""
		
		
		
		
	"""
	dy = dy + gravity
	dx *= (1.0-air_resistance)
	dy *= (1.0-air_resistance)
	
	if x >= WIDTH:
		x = WIDTH
		dx = dx * -1 * (1.0-friction)
	if x <= 0:
		x = 0
		dx = dx * -1 * (1.0-friction)
	if y <= 0:
		y = 0
		dy = dy * -1 * (1.0-friction)
	if y >= HEIGHT:
		y = HEIGHT
		dx = dx * -1 * (1.0-friction)
		dy = dy * -1 * (1.0-friction)
	return (x,y,dx,dy)



if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)