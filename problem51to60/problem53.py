# problem 53 
def combin(n,r):
	return frac(n) / ( frac(n-r) * frac(r))
	
	
def frac(n):
	prod = 1
	for i in range(1,n+1):
		prod = prod * i 
	return prod

count = 0
for n in range(1,101):
	for r in range(1,n+1):
		if combin(n,r) > 1000000:
			print "combin(" + str(n) + "," + str(r) + ") is larger than 1 million!"
			count += 1
			
print count
	
