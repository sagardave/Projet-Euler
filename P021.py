
def d(n):
	sum = 0
	for i in xrange(1, n/2 + 1, 1):
		if n%i == 0:
			sum += i
	return sum

cache = {}
sum = 0
for i in xrange(2, 10001, 1):
	cache[i] = d(i)
	if cache.get(cache[i]) == i and not i == cache[i]:
		sum += i + cache[i]

print sum
