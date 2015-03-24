sortedNamesList = sorted(eval(open("p022_names.txt").read()))

def stringToNum(name):
	return sum((ord(s) - 64) for s in name)

totalSum = 0
for i, name in enumerate(sortedNamesList):
	totalSum += stringToNum(name) * (i+1)

print totalSum


