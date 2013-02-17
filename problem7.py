import math

def generatePrime(n):
	p = range(2,n)
	p2 = range(2,n)
	for i in p:
		for j in range(2,int(math.ceil(math.sqrt(i)))+1):
			if i % j == 0:
				if i in p2:
					p2.remove(i)
	return p2 
p2 = generatePrime(105000)

# for some reason this list p2 does not contain 2
print p2[9999]
