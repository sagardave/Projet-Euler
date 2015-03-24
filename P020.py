
def getFactorial(n):
	if(n==0): 
		return 1
	else:
		return n * getFactorial(n-1)

num = getFactorial(100)
sum = sum(int(i) for i in str(num)) 
  

print sum
