# problem 27
# Idea: notice that by overservation, a and b are primes. There are not crezy many primes < 1000. We can iterate
# through them with their negative duals.
# This solution runs very fast, since half (?) of the cases will immidately return false due to neg poly eval value.
# but this also indicates that we may improve it further in choosing a and b. 
def generatePrime(n):
	p = range(2,n)
	p2 = range(2,n)
	for i in p:
		for j in range(2,i):
			if i % j == 0:
				if i in p2:
					p2.remove(i)
	return p2 

def isPrime(n):
	if n < 2:
		return False
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def evalPoly(a,b):
	cons = []
	for n in range(0, min(abs(a),abs(b))+1):
		if isPrime(n**2 + a* n + b):
			cons.append(n)
		else:
			return cons
	return cons
primes = []

primes = generatePrime(1000)

print primes

neg_primes = []
for i in primes:
	neg_primes.append(-1*i)
	neg_primes.append(i)

cons_s = []
cons_lens = []
for i in neg_primes:
	for j in neg_primes:
		print "eval: " + str(i) + ", " + str(j)
		cons = evalPoly(i,j)
		cons_s.append([cons,i,j])
		cons_lens.append(len(cons))

print max(cons_lens)
print cons_s[cons_lens.index(max(cons_lens))]
		
		
		
 
