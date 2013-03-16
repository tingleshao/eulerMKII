# problem 69

def gcd(a,b):
	while b != 0:
		t = b
		b = a % t
		a = t
	return a 


def phi(n):
	count = 1
	lst = []
	for i in range(2,n):
		if gcd(i,n) == 1:
			lst.append(i)
			count += 1
	return count
max_ratio = 2
last_n = 2
for n in range(2,1000001):
	update = True
	number_needed = int(float(n) / max_ratio) -1
	print n
	count = 1
	for i in range(2,n):
		if gcd(i,n) == 1:
			count += 1
		if count > number_needed:
			update = False
			break
	if update:
		ratio = float(n) / count
	if ratio > max_ratio:
		max_ratio = ratio
		last_n = n
		print 'upadate' + str(n)

print '----------'
print max_ratio
print last_n
