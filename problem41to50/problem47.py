# problem 47

prime_file = open('millionprimes.txt','r')
prime_lst = map(int,prime_file.readline().strip('[]').split(", "))
prime_lst.insert(0,2)

def hasFourDistinctPrimeFactor(n,prime_lst):
	divider_lst = []
	for i in prime_lst:
		if n % i == 0:
			divider_lst.append(i)
		if len(divider_lst) >= 4:
			return True
		if i > n :
			return False
a = 100000
b = 100001
c = 100002
d = 100003
while c < 200000:
	if hasFourDistinctPrimeFactor(a,prime_lst):
		if hasFourDistinctPrimeFactor(b,prime_lst):
			if hasFourDistinctPrimeFactor(c,prime_lst):
				if  hasFourDistinctPrimeFactor(d,prime_lst):
					print "foundOne: " + str(a)+ " " + str(b) + " " + str(c)  + " " + str(d)
					break
				else:
					a = d+1
					b = d+2
					c = d+3
					d = d+4
			else:
				a = d
				b = d+1
				c = d+2
				d = d+3
		else:
				a = c
				b = d
				c = d + 1
				d = d + 2
	else:
		a = b
		b = c
		c = d
		d = d + 1


				
