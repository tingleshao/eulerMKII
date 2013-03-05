# problem 45
# brute force solution takes several mins
def generateTriangle(n):
	lst = []	
	for i in range(1,n+1):
		tn = (i * (i+1)) / 2 
		lst.append(tn)

	return lst

def generatePentagonal(n):
	lst = []
	for i in range(1,n+1):
		pn = ( i * ( 3 * i - 1))  / 2 
		lst.append(pn)

	return lst

def generateHexagonal(n):
	lst = []
	for i in range(1,n+1):
		hn = i * ( 2 * i - 1)
		lst.append(hn)

	return lst


ts = generateTriangle(60000)
ps = generatePentagonal(50000)
hs = generateHexagonal(40000)
for i in ts:
	if i in ps and i in hs:
		print i 

