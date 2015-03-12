triangleArr = [[int(value) for value in line.split()] for line in open('P18.txt')]
size = len(triangleArr)

for i in xrange(size - 2, -1, -1):
	for j in xrange(i + 1):
		triangleArr[i][j] = max(triangleArr[i + 1][j], triangleArr[i + 1][j + 1]) + triangleArr[i][j]

print triangleArr[0][0]