# problem 63
# since 10**i has number of digits i+1
# if 9**i has number of digits less than i, we can stop 
count = 0
for i in range(1,1000000):
	for j in range(1,100):
		k = j**i
		if i == 1:
			print k
			print "----"
		len_k = len(str(k))
		if len_k == i:
			count += 1
		if len_k > i:
			print "from " + str(j) +", the " + str(i) + "th power's number of digits is larger than " + str(i)
			break
	if len(str(9**i )) < i:
		break
print count 
