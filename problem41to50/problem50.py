# problem 50
prime_file = open('millionprimes.txt', 'r')
prime_lst_str  = prime_file.readline()
prime_lst = map(int, prime_lst_str.strip('[]').split(", "))
prime_lst.insert(0,2)

sum = 0
ixx = 0
for p in prime_lst:
	sum = sum + p
	ixx += 1
	if sum >= 1000000:
		print sum
		print p 
		print ixx
		break
# ind =  547
sum2 = sum
max_len = 0
len_= 547
for i in range(50):
	end_p = prime_lst[547-i]
	sum = sum - end_p
	sum1 = sum
	for j in range(50):
		sum1 = sum1 - prime_lst[i]
		if sum1 in prime_lst:
			print "found one: " + str(sum1) + " from " +  str(j) + " to " + str(547-i)
			break
			
'''
print '--------'
for i in range(0,547):
	ind1 = 547 - prime_lst[i]
	if sum1 in prime_lst:
		print sum1
		print ind1
		break
	else:
		sum1 = sum1 - prime_lst[ind1]

print '------------------------'
for i in range(0,547):
	ind2  = i
	if sum2 in prime_lst:
		print sum2
		print ind2
		break
	else:
		sum2 = sum2 - prime_lst[ind2]

print "xxxxxx"
# now we have from 38 to 547: 998857  
#  and from 0 to 510: 959369
begin_prime_add = [2]
for i in range(1,37):
	begin_prime_add.append(prime_lst[i])
end_prime_add = [prime_lst[510]]
for i in range(1,37):
	end_prime_add.append(prime_lst[i+510])
print begin_prime_add
print end_prime_add
'''
print "-----Prove that from 7 to prime_lst[545] the sum is longest consective prime sum----"
ss = 0
for i in range(3,546):
	ss = ss+ prime_lst[i] 
print ss
	