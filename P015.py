#Using combinations formula
from math import factorial

def C(n,r):
	return factorial(n) / (factorial(r) * factorial((n - r)))

print C(40, 20)