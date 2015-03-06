import math
import time

def isPrime(num):
	for n in xrange (2,int(math.sqrt(num))+2):
		if (num % n == 0):
			return False
	return True;

def get_sum_of_prime_below(num):
	sum = 2
	for n in xrange(3, num, 2):
		if isPrime(n):
			sum = sum + n
	return sum

product = get_sum_of_prime_below(2000000)

print product
