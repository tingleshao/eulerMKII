# problem 35
import math
def generatePrime(n):
	p = range(2,n)
	p2 = range(2,n)
	for i in p:
		for j in range(2,int(math.ceil(math.sqrt(i)))+1):
			if i % j == 0:
				if i in p2:
					print i
					p2.remove(i)
	return p2 
p2 = generatePrime(1000000)
print "generate finished"
circular = []
def generateCircular(i):
	
	str_i  = str(i)
	len_i = len(str_i)
	lst = []
	for i in range(len_i):
		lst.append(int(str_i[:i]+str_i[i:]))
	return lst
for p in p2:
	flag = True
	lst = generateCircular(p)
	for pp in lst:
		if pp not in p2:
			flag = False
	if flag:
		print str(p) + "  is circular!"
		circular.append(p)
		
print circular
print len(circular)

f = open('millionprimes.txt','w')
f.write(str(p2))
f.close()