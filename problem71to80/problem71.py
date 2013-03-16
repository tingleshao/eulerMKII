# problem 71
# this is a pencil/paper problem
# 1000000 * 7 / 3 = 428571.xxxxx
# so the answert is 428570
# the following code takes a long time ( O(n^3) )
def gcd(a,b):
	while b != 0:
		t = b
		b = a % t
		a = t
	return a 

numerator_lst = []
denominator_lst = []

for d in range(1,1000):
	print d
	for n in range(1,d):
		hcf = gcd(n,d)
		nn = n / hcf
		dd = d / hcf
		flag = True
		for i in range(len(numerator_lst)):
			if float(nn) / dd > float(3) / 7:
				flag = False
				break
			elif float(nn) / dd == float(numerator_lst[i]) / denominator_lst[i]:		
				flag = False
				break
			elif float(nn) / dd < float(numerator_lst[i]) / denominator_lst[i]:
				numerator_lst.insert(i,nn)
				denominator_lst.insert(i,dd)
				flag = False
				break
		if flag:
			numerator_lst.append(nn)
			denominator_lst.append(dd)

for i in range(len(denominator_lst)):
	print str(numerator_lst[i]) + "/" + str(denominator_lst[i])
