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