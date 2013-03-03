# problem 39
# brute force search, the answer is 840 (max = 8) 
max = 0
maxp = 0
for i in range(1000):
	p = 1000-i
	count = 0
	for j in range(1,p-1):
		for k in range(j,p):
			if j**2 + k**2 == (p-j-k)**2:
				print "found one for p=" + str(p)
				count +=1
				break
	print "for p=" + str(p) + ": there are " + str(count) + " number of pairs"
	if count > max:
		max = count
		maxp = p
print max
print maxp