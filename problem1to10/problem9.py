# proj euler problem 9
akst = range(1,333)
for a in akst:
	for b in range(a+1, 500):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print a; print b; print c; 
			prod =  a * b * c
			break
			