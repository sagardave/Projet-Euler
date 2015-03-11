base_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
	"fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
base_decade_words = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"}
cache = {}
totalCount = 0;

def toWords(num, cache):
	wordToStr = str(num)
	lenCount = len(str(num))
	numToWord = ""
	restOfNum = 0
	if (num < 21):
		return base_words[num-1]
	elif(num%(10**(lenCount-1)) == 0):
		if lenCount-1 == 1:
			return base_decade_words.get(num) if base_decade_words.get(num) else (base_words[num/10 - 1] + "ty").replace("tt", "t")
		elif lenCount-1 == 2:
			return base_words[num/100 - 1] + "hundred"
		else:
			return "onethousand"
	else:
		if(num < 100):
			for n in range(lenCount-1, -1, -1):
				currentNum = (num - (num%(10**n)))/(10**n) if num > 10 else num
				if (n == 0):
					numToWord = numToWord + base_words[num-1]
				else:
					tmp = base_decade_words.get(currentNum * 10**n) if base_decade_words.get(currentNum * 10**n) else base_words[num/10 - 1] + "ty"
					numToWord = numToWord + tmp
				num = num - currentNum*10					
		else:
			firstNum = (num - (num%(10**(lenCount-1))))/(10**(lenCount-1))
			restOfNum = num - (firstNum*100)
			numToWord = numToWord +  base_words[firstNum-1] + "hundredand" + cache[restOfNum]

	numToWord = numToWord.replace("tt", "t")
	cache[num] = numToWord
	return numToWord

for num in xrange(1,1001,1):
	cache[num] = toWords(num, cache)
	totalCount = totalCount + len(cache[num])
print totalCount
