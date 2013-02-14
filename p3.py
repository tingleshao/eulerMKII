# proj euler problem 3
import math
n = 600851475143
def generatePrime(n):
	p = range(2,n)
	p2 = range(2,n)
	for i in p:
		for j in range(2,i):
			if i % j == 0:
				if i in p2:
					p2.remove(i)
	return p2 
	
#print generatePrime(100)	
# try generatePrime(100)
p = generatePrime(1000)
for i in p:
	if n % i == 0:
		print i
print "___"
n2 = n / 71
for i in p:
	if n2 % i == 0:
		print i
print "___"
n3 = n2 / 839
p2 = generatePrime(2000)

for i in p2:
	if n3 % i == 0:
		print i
print "___"
n4 = n3 / 1471
p2 = generatePrime(6857)
print p2
for i in p2:
	if n4 % i == 0:
		print i