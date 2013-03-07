# problem 52
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



lst = permute('123456789')
print "permutation complete"
lst2 = []
previous = 0
for s in lst:
	ss = int(s[:-3])
	if ss != previous:
		lst2.append(ss)
		print ss
		previous = ss
	
#print lst2
ddlLst = []
for i in lst2:
	if i * 6 > 1000000:
		break
	if 2 * i in lst2 and 3 * i in lst2 and 4 * i in lst2:
		print str(i) + " " + str(2*i) + " " + str(3*i) + " " + str(4*i) + " are ok but..."
		if 5 *i in lst2 and 6 * i in lst2:
			print "good!" 
			ddlLst.append([i,i*2,i*3,i*4,i*5,i*6])
		else:
			print "not good enough"
print "---------------------------------------"
			
for d in ddlLst:
	print d