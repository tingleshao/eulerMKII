# problem 58
import math
prime_file = open('millionprimes.txt', 'r')
prime_lst_str  = prime_file.readline()
prime_lst = map(int, prime_lst_str.strip('[]').split(", "))
prime_lst.insert(0,2)
# the 1 million primes list does not work after curr exceeds 1000000
diag_lst = [1]
	
curr = 1
diff = 2
new_four = []
prime_count = 0

def is_prime(d):
	for i in range(2,int(math.sqrt(d))+1):
		if d % i == 0:
			return False
	return True

for k in range(1,30000):
	for j in range(4):
		curr = curr + diff
		diag_lst.append(curr)
		new_four.append(curr)
	diff += 2
	if k == 749:
		print curr
   
	
	for d in new_four:
		if d < 1000000:
			if d in prime_lst:
				prime_count +=1
		elif is_prime(d):
			prime_count +=1

	if float(prime_count) / len(diag_lst) < 0.1:
		print k
		print "less than 10%!"
		print k * 2 + 1
		break
	print str(k) + ": " + str(float(prime_count) / len(diag_lst))
	new_four = []


