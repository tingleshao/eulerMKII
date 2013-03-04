# problem 42
dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

word_file = open('words.txt')
word = word_file.readline()
word_lst = word.strip('""').split('","')
for word in word_lst:
	print word

def calculate_score(word):
	score = 0
	for c in word:
		if dict.has_key(c):
			score = score + dict[c]
	return score

# estimation: calculate up to 100
def isTriangle(n):
	n = n * 2
	for i in range(1,100):
		if i * ( i + 1 ) == n:
		#	print str(n) + " is triangle! "
			return True
	return False

count = 0
for word in word_lst:
	score = calculate_score(word)
	if isTriangle(score):
		print word + " is triangle!"
		count = count+1
print count
