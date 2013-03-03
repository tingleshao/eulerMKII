# problem 38 
# Is it true that the largest number found for n = 1..2 have to yield the 
#  largest result? 
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
lst = permute('123456789')
print 'permutation complete'
n = 98765
for i in range(len(lst)):
	ind = len(lst)  - 1
	new_n = int(lst[ind-i][0:4])
	if new_n != n:
		n = new_n
		print n
		if ( str(n) + str(n*2) ) in lst:
			print 'found one'
			print n
			break
		
		