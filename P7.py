import math;

def isPrime(num):
	for n in range (2,int(math.sqrt(num))+2):
		if (num % n == 0):
			return False;
	return True;

num = 1;
count = 2;
while(count < 10002):
	num = num + 2;
	if(isPrime(num)):
		count = count + 1;
	

print num;