# problem 41
# it is shown that the prime for pandigital requirement from 1~9 or 1~8 cannot be found. 
import math
def permute(lst):
	if len(lst) == 1:
		return lst
	else:
		ret_lst = []
		for i in range(len(lst)):
			remain = lst[:i]+lst[i+1:]
			took = lst[i]
			for g in permute(remain):
				ret_lst.append(took+g)
		return ret_lst

# test
def isPrime(n):
	for i in range(2,int(math.ceil(math.sqrt(n)))):
		if n % i == 0:
			print str(n) +" is not prime"
			return False
	return True



lst = permute('1234567')
print 'permutation complete'
res = []
for i in range(len(lst)):
	ind = len(lst)  - 1
	n = int(lst[ind-i])
	if isPrime(n):
		print str(n) + " is prime"
		break
		


		
		
