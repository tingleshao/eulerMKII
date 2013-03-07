# problem 49
prime_file = open('millionprimes.txt', 'r')
prime_lst_str  = prime_file.readline()
prime_lst = map(int, prime_lst_str.strip('[]').split(", "))
prime_lst.insert(0,2)

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

# get the indices of the first and last primes
flag = False
for i in prime_lst:
	
	if i >= 1000 and not flag:
		print prime_lst.index(i)
		flag = True
	if i >= 10000:
		print prime_lst.index(i)
		break
# 168 and 1229 

def unique_lst(lst):
	u_lst = []
	for i in lst:
		if i not in u_lst:
			u_lst.append(i)
	return u_lst
prime_permute_lsts = []
for ind in range(168,1229):
	prime = prime_lst[ind]
	all_permute = unique_lst(map(int,permute(str(prime))))
	prime_permutes = []
	for i in all_permute:
		if i in prime_lst and i >= 1000 and i < 10000:
			prime_permutes.append(i)
	prime_permutes.sort()
	if len(prime_permutes) >= 3 and prime_permutes not in prime_permute_lsts:
		print "found one! : " + str(prime_permutes)
		prime_permute_lsts.append(prime_permutes)

# count diffs to get the desired permutes
#def diff_hash_greater_than_three(diff_lst):
#	hash = {}
#	for d in diff_lst:
#		if hash.has_key(d):
#			hash[d] += 1
#		else:
#			hash[d] = 1
#	for k in hash:
#		if hash[k] >= 3:
#			print k
#			return True
#	return False
	
#def generate_diff_lst(pp):
#	diff_lst = []
#	for i in range(len(pp)-1):
#		p1 = pp[i]
#		for j in range(i+1, len(pp)):
#			diff_lst.append(pp[j] - p1)
#	return diff_lst
	
for pp in prime_permute_lsts:
	for i in range(len(pp)-1):
		p1 = pp[i]
		for j in range(i+1,len(pp)):
			if pp[j] + (pp[j] - p1) in pp:
				print '--------'
				print p1
				print pp[j]
				print pp[j] + (pp[j] - p1)
#	if diff_hash_greater_than_three(diff_lst):
#		print pp
	

#lst = permute('123456789')
#res = []
#for i in range(len(lst)):
#	ind = len(lst)  - 1
#	n = int(lst[ind-i][:])
#	if isPrime(n):
#		print str(n) + " is prime"
#		break
		


		
		
