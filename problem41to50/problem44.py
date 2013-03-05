# problem 44 
# staight forward solution 
# 2166 was calculated from first run from 1 to 10000
def generatePentagonLst(n):
	lst = []
	for i in range(1,n+1):
		lst.append( i * (3 * i - 1)/ 2 )
	return lst

def checkIfPentagonal(lst,i,j):
	if i + j not in lst:
		return False
	if i - j not in lst and j - i not in lst:
		return False
	return True

pta_lst = generatePentagonLst(10000)
min_diff = 100000000
print pta_lst.index(7042750)
print pta_lst[:10]
for i in range(2166,len(pta_lst)):
	flag = False
	for j in range(0,i):
		pk = pta_lst[i]
		pj = pta_lst[i-j-1]
		if checkIfPentagonal(pta_lst,pk,pj):
			print abs(pk-pj)
			print str(pj) + " and " + str(pk) + " are pentagonal"
			if abs(pk-pj)  < min_diff:
				min_diff = abs(pk-pj)
			break
print min_diff

