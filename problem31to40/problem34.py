# problem 34
# estimate up to 200000
def frac(i):
	prod = 1
	if i == 0:
		return 1
		
	for j in range(1,i+1):
		prod = prod * j
	return prod

curious = []
for i in range(200001):
	digits = list(str(i))
	sum = 0
	for d in digits:
		sum = sum + frac(int(d))
	if sum == i:
		print "found one!"
		curious.append(i)
		
sum = 0
print curious
for i in curious:
	sum = sum + i
print sum