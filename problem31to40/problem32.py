# problem 32

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
lst = permute('0123456789')
pand = []
for i in lst:

	print "------------"
	print i
	for j in range(1,8):
		a = int(i[:j])
		for k in range(j+1,9):
			b = int(i[j:k])
			c = int(i[k:])
			print a
			print b
			print c
			if a * b == c:
				print "find One!"
				if c not in pand:
					pand.append(c)
print pand

# [5796, 4396, 7632, 6952, 5346, 7254, 7852, 16038, 21658, 26910, 17082, 17820, 19
#084, 20457, 20754, 24507, 15628, 27504, 15678, 28651, 32890, 28156, 36508, 34902
#, 58401, 65128, 65821] is the answer for 0~9..
# for answer to 1~9, we choose the four digit subset 
# sum is 45228