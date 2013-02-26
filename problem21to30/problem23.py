# problem 2
'''
import math
def checkIfAbun(n):
	div = []
	for i in range(1,n):
		if n % i == 0:
			if not i in div:	
				div.append(i)
	sum = 0
	for i in div:
		sum = sum + i
	if sum > n:
		return True
		
all_n = range(1,28124)

abun_lst = []
for i in all_n:
	if checkIfAbun(i):
		abun_lst.append(i)
		
print abun_lst[0]
'''
f = open('abun_lst.txt')
abun_lst_str = f.readline()[1:-1]

abun_lst = map(int,abun_lst_str.split(','))
not_sum_abun_lst = range(1,23124)
all_n = range(1,23124)

for i in all_n:
	print i
	print '...'
	for j in abun_lst:
		if i - j in abun_lst:
			not_sum_abun_lst.remove(i)
			print "no"
			break
	print "yes"
		
print not_sum_abun_lst
sum = 0 
for i in not_sum_abun_lst:
	sum = sum + i 
print sum

