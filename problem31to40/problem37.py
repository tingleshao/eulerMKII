# problem 37
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
	p2.insert(0,2)
	return p2 
	
def findTruncable(p,p2):
	str_p = str(p)
	for i in range(len(str_p)):
		left_trun_p = int(str_p[i:])
		right_trun_p = int(str_p[:i+1])
		if left_trun_p not in p2:
			return False
		if right_trun_p not in p2:
			return False
			
	return True
p2 = generatePrime(100000)
print p2
truncable = []
for i in p2:
	if findTruncable(i,p2):
		print "found one@"
		truncable.append(i)
print truncable
sum = 0
print "len: " + str(len(truncable)-4)
for i in truncable:
	sum += i
print sum

# the last one was obtained by observation: 739397
# the observation can be converted into code once we have the prome table from 1~ 100000
# and from google I know 739397 is indeed a prime....

