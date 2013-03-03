# problem 197
# the u will converge to a number after several iterations... we don't need to calculate up to n = 10^12.
import math
def f(n):
	return math.floor(2**(30.403243784-n**2)) * 10**(-9)
u = -1
u_1 = u
for i in range(30000):
	u = f(u_1)
	u_1 = f(u)
	u+u_1
	print u
	
print u+u_1