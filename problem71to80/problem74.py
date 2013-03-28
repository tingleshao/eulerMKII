# problem 74
def factorial(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 6
	elif n == 4:
		return 24
	elif n == 5:
		return 120
	elif n == 6:
		return 720 
	elif n == 7:
		return 5040
	elif n == 8:
		return 40320
	elif n == 9:
		return 362880
len_lst = []
total_count = 0
for i in range(1,1000000):
	print "-----------"
	print i
	dd = i
	sum_ = 0
	lst = []
	while True:
		sum_ = 0
		for d in str(dd):
			sum_ = sum_ + factorial(int(d))
		if sum_  in lst:
			len_lst.append(len(lst))
			if i == 78:
				print "--------"
				print lst
				print "88888"
			if len(lst) == 59:
				total_count += 1
				print "-->>>>>" + str(i)
			break
		lst.append(sum_)
		dd = sum_
print total_count
		
print "max: " +str( max(len_lst)	)
		
		
		
