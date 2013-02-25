# problem 25
a = 1
b = 1
count = 2
for i in range(10000):
	c = a + b 
	a = b
	b = c
	count = count + 1
	if len(str(c)) > 999:
		print count
		break
print count