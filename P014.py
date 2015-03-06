def isEven(num):
	return True if num % 2 == 0 else False

def getCollatzChainCount(num, cache):
	seqNum = num
	count = 0;
	while(seqNum != 1):
		if (cache.get(seqNum)):
			count = count + cache[seqNum] - 1
			seqNum = 1;
		else:
			seqNum = seqNum/2 if isEven(seqNum) else (3 * seqNum + 1)
			count = count + 1

	return count + 1

cache = {}
maxCount = 0
currentCount = 0
maxStartingNum = 0;
for n in range(3,1000000):
	currentCount = getCollatzChainCount(n, cache)
	cache[n] = currentCount
	if (currentCount > maxCount):
		maxCount = currentCount
		maxStartingNum = n

print maxStartingNum
