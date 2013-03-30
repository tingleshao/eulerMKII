# problem 85
# http://blog.dreamshire.com/2009/03/27/project-euler-problem-85-solution/
# formula : (x^2 + x) (y^2 + y) / 4
import math
diff = 2000000
flag = False
diffs = {'min':[0,0,2000000]}
for n in range(1, 1000):
	for m in range(n, 1000):
		print m
		print n 
		print "-----"
		count = (m ** 2 + m ) * ( n ** 2 + n ) / 4
		curr_diff = abs(2000000 - count )
		if curr_diff < diffs['min'][2]:
			diffs['min'] = [m,n,curr_diff]
print diffs['min']
