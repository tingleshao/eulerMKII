# project euler problem 6 
# 
#100 * 101 / 2 = 5050
# 5050 ** 2 = 25502500
sum = 0
for i in range(101):
	sum = sum + i **2
	
print 25502500 - sum 