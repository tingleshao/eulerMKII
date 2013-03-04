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

prime_file = open('millionprimes.txt', 'r')
prime_lst_str  = prime_file.readline()
prime_lst = map(int, prime_lst_str.strip('[]').split(", "))
prime_lst.insert(0,2)
#p2 = generatePrime(1000000)
print "generate finished"
circular = []
def generateCircular(i):
	
	str_i  = str(i)
	len_i = len(str_i)
	lst = []
	for i in range(len_i):
		lst.append(int(str_i[i:]+str_i[:i]))
	return lst
	
for p in prime_lst:
	flag = True
	if '2' in str(p) or '4' in str(p) or '5' in str(p) or '6' in str(p) or '8' in str(p) or '0' in str(p):
		print str(p) + " is not circular!"
		flag = False
	else:
		lst = generateCircular(p)
		print lst
		for pp in lst:
			if pp not in prime_lst:
				print str(p) + " is not circular!"
				flag = False
				break
	if flag:
		print str(p) + "  is circular!"
		circular.append(p)
		
print circular
print len(circular)+2

#f = open('millionprimes.txt','w')
#f.write(str(p2))
#f.close()