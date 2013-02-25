# problem 20
frac = 1
for i in range(1,101):
	frac = frac * i 
fraclst = map(int,list(str(frac)))
print frac
print fraclst
sum = 0
for i in fraclst:
	sum = sum + i
print sum