# project euler problem 14
start = 1
lst = []
def go_back(n):
	for i in range(100):
		if (n - 1) % 3 == 0 and (n - 1) / 3 > 1:
			n = (n - 1) / 3
		else:
			n = n * 2
		lst.append(n)
	return lst

lst = go_back(start)
print lst
print len(lst)

lst2 = []
def go_forward(n):
	lst2 = []
	while n > 1:
		if n % 2 == 0:
			n = n /2
		else:
			n = n * 3 + 1
		lst2.append(n)
	lst2.append(1)
	return lst2
len_lst = []
for i in range(1000000):
	j = 1000000 - 1 - i
	len_lst.append(len(go_forward(j)))
	if len_lst[-1] == 525:
		print j
		break
	#print len_lst[-1]
	
#print max(len_lst)