# project euler problem 12
# brute force solution
tri = [1]
for i in range(2,10000):
	tri.append(tri[-1]+i)
	
print tri

# list 124750's divisors
divisors = []
max_divisors = []
max_len_div = 0
for j in range(4999,len(tri)):
	x = tri[j]
	for i in range(1,x+1):
		if x % i == 0:
			divisors.append(i)
	if max_len_div < len(divisors):
		max_len_div = len(divisors)
		max_divisors = divisors
	if max_len_div >= 500:
		break
	divisors = []

print max_len_div; print max_divisors
