# problem 70
# http://www.mathblog.dk/project-euler-70-investigate-values-of-n-for-which-%CF%86n-is-a-permutation-of-n/

phi_best = 1
best = 1
best_ratio = 100000000


def is_prime(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

limit = 10000000
prime_lst = []
for n in range(2000,5001):
	if is_prime(n):
		prime_lst.append(n)

for i in prime_lst:
	for j in prime_lst:
		n = i * j 
		if n > limit:
			break
		phi = (i - 1) * (j-1)
		ratio = float(n) / phi
		n_sort = list(str(n))
		n_sort.sort()
		phi_sort = list(str(phi))
		phi_sort.sort()
		if phi_sort == n_sort and best_ratio > ratio:
			best = n
			phi_best = phi
			best_ratio = ratio


print "best: "+ str(best)
print "phi_best: " + str(phi_best)
print "best_ratio: " + str(best_ratio)
 
