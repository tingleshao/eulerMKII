# problem 57
a_lst = [1,3]
b_lst = [1,2]
ind = 2
for i in range(998):
	a_lst.append(a_lst[ind-1] * 2 + a_lst[ind-2])
	b_lst.append(b_lst[ind-1] * 2 + b_lst[ind-2])
	ind+=1
print a_lst[0:10]
print b_lst[0:10]
count = 0
for i in range(len(a_lst)):
	if len(str(a_lst[i])) > len(str(b_lst[i])):
		count +=1
		
print count