# problem 30
# try 1 to 10000
lst = []
# just estimate the values are between 1 to 1000001
for i in range(1000001,2000001):
	str_i = str(i)
	sum_ = 0		
	for c in str_i:
		sum_ = sum_ + int(c) ** 5
	if sum_ == i:	
		lst.append(i)

print lst
