# problem 65
# there is a closed form fomula for the numerator 
n_lst = [2,3]
e_lst = []
for i in range(1,99/3+1):
	e_lst.append(1)
	e_lst.append(2*i)
	e_lst.append(1)
# print e_lst
ind = 2
for i in range(len(e_lst)-1):
	n_lst.append(n_lst[ind-1]*e_lst[i+1]+n_lst[ind-2])
	ind+=1

print n_lst
print len(n_lst)	
last_term = str(n_lst[-1])
sum = 0
for d in last_term:
	sum = sum + (int(d))

print sum
