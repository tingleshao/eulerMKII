# problem 43
# this is just a translation of the problem.
# a more clever solution would be find the compositions in the prime list that 
# fufills the property
'''
1406357289 is divisible
1430952867 is divisible
1460357289 is divisible
4106357289 is divisible
4130952867 is divisible
4160357289 is divisible
16695334890
'''
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
def isSubDivisible(i):
	i_1 = int(i[1:4]) 
	i_2 = int(i[2:5])
	i_3 = int(i[3:6])
	i_4 = int(i[4:7])
	i_5 = int(i[5:8])
	i_6 = int(i[6:9])
	i_7 = int(i[7:10])
	if i_1 % 2 != 0:
		return False
	if i_2 % 3 != 0:
		return False
	if i_3 % 5 != 0:
		return False
	if i_4 % 7 != 0:
		return False
	if i_5 % 11 != 0:
		return False
	if i_6 % 13 != 0:
		return False
	if i_7 % 17 != 0:
		return False
	return True
# test
lst = permute('0123456789')
print 'permutation complete'
subdivisible = []
sum = 0
for i in lst:
	if isSubDivisible(i):
		print str(i) + " is divisible"
		subdivisible.append(i)
for i in subdivisible:
	sum = sum + int(i)
print sum


