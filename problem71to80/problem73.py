# problem 73
# takes a long time 
def gcd(a,b):
	while b != 0:
		t = b
		b = a % t
		a = t
	return a 

numerator_lst = []
denominator_lst = []
#count = 0
for d in range(1,12001):
	print d
	for n in range(1,d):
		fn = float(n)
		flag = True
		if fn / d >= 1.0 / 2:
			flag = False
			break
		elif fn / d <= 1.0 / 3:
			flag = False
		if flag:	
			hcf = gcd(n,d)
			nn = n / hcf
			dd = d / hcf
			numerator_lst.append(nn)
			denominator_lst.append(dd)
#			count += 1
#	print str(d) + ": " + str(count)
#print count
new_n = []
new_d = []
print "first stage finished"
for i in range(len(denominator_lst)):
	flag = True
	for j in range(len(new_n)):
		if numerator_lst[i] == new_n[j] and denominator_lst[i] == new_d[j]:
			flag = False
			break
	if flag:
		print str(numerator_lst[i])+"/"+str(denominator_lst[i])
		new_n.append(numerator_lst[i])
		new_d.append(denominator_lst[i])
print len(new_n)
	
			
