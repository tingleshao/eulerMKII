# problem 31
# recursive way in computing money exhcange
# may switch to dynamic programming for coin exchange
money = [1,2,5,10,20,50,100,200]
money.reverse()
#ways_mat = []
#for i in range(200):
#	ways_mat.append([0,0,0,0,0,0,0,0])

#def exchangeUseMoney(c,m):
#	subMoney = []
#	for i in money:
#		if i <= c:
#			subMoney.append(i)
#	for 
#	exchangeUseMoney(
#for m in range(1,10):
#	ways = 0
#	if m in money:
#		ways = ways + 1
#	for c in money:
#		if c < m:
#			ways = ways + ways_lst[m-c-1]
#			print "use "+ str(c) + ": " + str(ways_lst[m-c-1])
#	ways = ways + 1
#	ways_lst[m-1] = ways
#	print str(m) + ": " + str(ways) + ' ways'
#	print " -------"

#print ways_lst
def useSubMoney(coin_i,m):
	c = money[coin_i]
	way = ""
	if m == 0:
		return way
	if c <= m:
		way = way + str(c)
		way = way + useSubMoney(coin_i,m-c)
	else:
		way = way + useSubMoney(coin_i+1,m)
	return way

def allWithUseSubMoney(coin_i,m):
	ways = ""
	c = money[coin_i]
	can_have = m / c
	print can_have
	print range(can_have)
	ways = ways + useSubMoney(coin_i,m) + "\n"
	for j in range(1,8-coin_i):	
		for i in range(can_have):
			way = str(c)*i + useSubMoney(coin_i+j,m-i*c)	
			way = way + "\n"
			ways = ways + way
	return ways 

print allWithUseSubMoney(5,7)
print allWithUseSubMoney(6,7)
print allWithUseSubMoney(7,7)
