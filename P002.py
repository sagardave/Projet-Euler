sum = 0;
prev1 = 1;
prev2 = 1;
current = 0;
while current <= 4000000:
	current = prev1+ prev2;
	prev2 = prev1;
	prev1 = current;
	if (current % 2 == 0):
		sum = sum + current;

print sum;
