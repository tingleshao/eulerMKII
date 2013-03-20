# problem 97
p = 2 ** 40
for i in range(7830417):
	p = p * 2
	p = int(str(p)[-10:])
	print 
	print i
p = p * 28433
p = p + 1
print p 
