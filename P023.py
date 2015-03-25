def isAbundantNum(num):
	sum = 0
	for i in xrange(1, num/2 + 1, 1):
		if num%i == 0:
			sum += i
	return sum > num

num = 0
totalSum = 0
summableDict ={}
abundantNums = []
for num in xrange(28123):
	if isAbundantNum(num):
		summableDict[num+num] = True
		abundantNums.append(num)
		for n in abundantNums:
			if not n == num:
				summableDict[num+n] = True
	num += 1

for x in xrange(28123):
	if not summableDict.get(x):
		totalSum += x

print totalSum
