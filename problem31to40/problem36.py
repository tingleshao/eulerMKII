# problem 36

def checkPalin(i):
	i_lst = list(i)
	i_lst.reverse()
	i_rev = "".join(i_lst)
	return i_rev == i
palin = []
for i in range(1,1000001):
	if checkPalin(str(i)):
		bin_i = bin(i)[2:]
		if not bin(i)[-1] == '0':
			if checkPalin(bin_i):
				print "find palin!"
				palin.append(i)
print palin
sum = 0
for i in palin:
	sum = sum + i
print sum