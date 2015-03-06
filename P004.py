
def isPalindrome(num):
	if(str(num) == str(num)[::-1]):
		return True;
	else:
		return False;

maxPalindrome = 0;
currentNum = 0;
for i in range (100,1000):
	for j in range(100,1000):
		currentNum = i * j;
		if(isPalindrome(currentNum) and currentNum > maxPalindrome):
			maxPalindrome = currentNum 
print maxPalindrome;

