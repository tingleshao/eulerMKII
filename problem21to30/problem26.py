# problem 26
# 997 is the maximum number of stack length python can have, 
#if the question asks a limit >> 1000, it is necessary to come up with a more clever solution.

def detectLoop(i,n, count):
	i = i * 10
	lst = ""
	if count >= 997:
		return lst
	if i / n > 0:
		lst = lst + str(i / n)
		if i % n != 0:
			lst = lst + detectLoop(i % n, n, count + 1)
	else: 
		lst = lst + '0'
		lst = lst + detectLoop(i % n , n , count+1)
	return lst
looplens = []
num = []
for i in range(2,1000):	
	a = detectLoop(1,i,0)
	print "0."+ a
	if len(a) == 997:
		last = a[-4:]
		loopLen = len(a.split(last)[1])+4
		print "------"
		print "[" + str(i) + "]"
		print a.split(last)[1]+last
		print loopLen
		looplens.append(loopLen)
		num.append(i)
print max(looplens)
#982 was derived from one run of max(looplens)
print num[looplens.index(982)]

print detectLoop(1,982,0)