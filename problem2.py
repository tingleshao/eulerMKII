# project euler problem 2

#start with 3 and 5 
sum = 0
a = 3
b = 5
while a+b < 4000000:
	sum = sum + a + b
	c = a + b
	a = b + c
	b = a + c
	
sum = sum + 2
print sum