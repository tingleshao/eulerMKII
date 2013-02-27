# problem 24
# brute force recursion approach
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
print lst[1000000-1]
