# problem 78
# http://www.mathblog.dk/project-euler-78-coin-piles/
def foo():
	pn_lst = [1]
	n = 1
	while True:
		i = 0
		penta = 1
		pn_lst.append(0)

		while penta <= n:
			sign = -1 if i % 4 > 1 else 1
			pn_lst[n] += sign * pn_lst[n-penta]
			pn_lst[n] %= 1000000
			i+=1 
			j =  i / 2 + 1 if (i%2==0) else -(i/2+1)
			penta = j * (3 * j -1) /2 
		if pn_lst[n] == 0:
			break
		n+=1
		print n 
	print n 

import timeit
print timeit.timeit('foo()',number = 1,setup = "from __main__ import foo")

# takes 11.837461858s
