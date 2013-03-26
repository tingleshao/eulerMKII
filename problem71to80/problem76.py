# problem 76
# similar to problem 78
pn_lst = [1]
n = 1
while True:
	i = 0
	penta = 1
	pn_lst.append(0)
	while penta <= n:
		sign = -1 if i % 4 > 1 else 1
		pn_lst[n] += sign * pn_lst[n-penta]
		#pn_lst[n] %= 1000000
		i+=1 
		j =  i / 2 + 1 if (i%2==0) else -(i/2+1)
		penta = j * (3 * j -1) /2 
	if n == 101:
		break
	n+=1
print pn_lst[100]
