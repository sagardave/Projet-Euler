import math

dictForDistinctTerms = {}
for i in range(2, 101, 1):
	for j in range(2, 101, 1):
		dictForDistinctTerms[math.pow(i,j)] = True

print (str(len(dictForDistinctTerms)))
