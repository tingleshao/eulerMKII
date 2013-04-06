# problem 64
# http://www.mathblog.dk/project-euler-continued-fractions-odd-period
import math

def loop_length(n):
	m = 0.0
	d = 1.0
	a = math.floor(math.sqrt(n))
	S = float(n)
	param_lst = [[m,d,a]]
	loop_len = 0
	for i in range(1000):
		m1 = d * a - m 
	#	print "m: " + str(m1)
		d1 = (S - m1 ** 2) / d 
	#	print "d: " + str(d1)
		a1 = math.floor( (math.sqrt(S) + m1) / float(d1) )
	#	print "a: " + str(a1)
		if [m1,d1,a1] in param_lst:
		# why we can instread check a1 == 2 * a0 here? 
			return len(param_lst) - param_lst.index([m1,d1,a1])
		d = d1
		a = a1
		m = m1
		param_lst.append([m,d,a])
	
count= 0

for i in range(2,10001):
	if math.sqrt(i) % 1 != 0:
		#print "i: " + str(i)
		lop_len = loop_length(i)		
		if lop_len % 2 == 1:
			count += 1
print count
