def getNumOfDigits(num):
	return len(str(num))

reachedThousand = False
fibn = [1, 1]
i = 2
while(reachedThousand == False):
	fibn.append(fibn[i-1] + fibn[i-2])
	reachedThousand = getNumOfDigits(fibn[i]) == 1000
	i = i + 1
print ("n = " + str(i))