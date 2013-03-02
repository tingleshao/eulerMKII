# problem 33
def gcd(a,b):
	while b != 0:
		t = b
		b = a % t
		a = t
	return a
stro = []
for i in range(11,101):
	print "---------"
	jrange =  range(10,i)
	for j in jrange:
		gd = gcd(i,j)
		istr1 = list(str(i))
		jstr1 = list(str(j))
		ii = i / gd
		jj = j / gd
		istr2 = str(ii)
		jstr2 = str(jj)
		if not (len(istr2) != 1 or len(jstr2) !=1) and not (istr2 not in istr1 or jstr2 not in jstr1):
			istr1.remove(istr2)
			jstr1.remove(jstr2)
			if istr1 == jstr1 and istr1 != ['0']:
				print gd
				print  istr1
				print  jstr1
				print i 
				print j 
				stro.append([i,j])
print stro
# and include 48 / 98 in the problem.......
			