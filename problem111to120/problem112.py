# problem 112 
# boundcy numbers
def isDECorINC(n):
	n_lst = map(int, list(str(n)))
	if len(n_lst) <= 2:
		return True
	if n_lst[0] < n_lst[1]:
		return isINC(n_lst[1:])
	if n_lst[0] > n_lst[1]:
		return isDEC(n_lst[1:])
	return isDECorINC(int("".join(map(str,n_lst[1:]))))




	
def isDEC(n_lst):
	if len(n_lst) == 1:
		return True
	if n_lst[0] < n_lst[1]:
		return False
	return isDEC(n_lst[1:])

def isINC(n_lst):
	if len(n_lst)== 1:
		return True
	if n_lst[0] > n_lst[1]:
		return False
	return isINC(n_lst[1:])

bouncy_count = 0  
for i in range(1,2000001):
	if not isDECorINC(i):
		print str(i) + " is bouncy "
		bouncy_count += 1
	else:
		print str(i) + ' is not bouncy'
	if i > 1500000:
		if bouncy_count / float(i) == 0.99:
			print i 
			break

print bouncy_count / 2000000.0
