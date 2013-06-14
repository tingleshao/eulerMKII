# problem 102
# If all ys or all xs have the same sign, (including zero case) the triangle does not contain 
#  the origin.
# If two of them have the same sign while the other one has the opposite sign, then check the zero
#  crossing between that one and the other two. If the zero crossings have opposite sign, then 
#  the triangle contains the origin, otherwise it does not. 
# This covers all the cases.

def containsOrigin(x1,y1,x2,y2,x3,y3):
	if (x1 >= 0 and x2 >= 0 and x3 >= 0):
		return False
	if (x1 <= 0 and x2 <= 0 and x3 <= 0):
		return False
	if (y1 >= 0 and y2 >= 0 and y3 >= 0):
		return False
	if (y1 <= 0 and y2 <= 0 and y3 <= 0):
		return False
	if (y1 >= 0 and y2 <= 0 and y3 <= 0):
		# check the x axis intersection between p1-p2 and between p1-p3 
		cross1 = x1 - (x1-x2)*(y1/(y1-y2))
		cross2 = x1 - (x1-x3)*(y1/(y1-y3))
		if cross1 * cross2 < 0:
			return True
		return False
	if (y1 < 0 and y2 > 0 and y3 < 0):
		# check the x axis intersection between p1-p2 and p2-p3 
		cross1 = x2 - (x2-x1)*(y2/(y2-y1))
		cross2 = x2 - (x2-x3)*(y2/(y2-y3))
		if cross1 * cross2 < 0:
			return True
		return False
	if (y1 < 0 and y2 < 0 and y3 > 0):
		# p1-p3 and p2-p3
		cross1 = x3 - (x3-x1)*(y3/(y3-y1))
		cross2 = x3 - (x3-x2)*(y3/(y3-y2))
		if cross1 * cross2 < 0:
			return True
		return False
	if (y1 > 0 and y2 > 0 and y3 < 0):
		# p1-p3 and p2-p3
		cross1 = x3 - (x3-x1)*(y3/(y3-y1))
		cross2 = x3 - (x3-x2)*(y3/(y3-y2))
		if cross1 * cross2 < 0:
			return True
		return False
	if (y1 > 0 and y2 < 0 and y3 > 0):
		# p1-p2 and p2-p3
		cross1 = x2 - (x2-x1)*(y2/(y2-y1))
		cross2 = x2 - (x2-x3)*(y2/(y2-y3))
		if cross1 * cross2 < 0:
			return True
		return False
	if (y1 < 0 and y2 > 0 and y3 > 0):
		# p1-p2 and p1-p3
		cross1 = x1 - (x1-x2)*(y1/(y1-y2))
		cross2 = x1 - (x1-x3)*(y1/(y1-y3))
		if cross1 * cross2 < 0:
			return True
		return False


count = 0


triangle_txt = open("triangles.txt",'r')
for i in range(1000):
	line = triangle_txt.readline()
	xy_arr = map(float,line.strip().split(","))
	if containsOrigin(xy_arr[0],xy_arr[1],xy_arr[2],xy_arr[3],xy_arr[4],xy_arr[5]):
		count += 1
	if i == 0 or i == 1:
		print containsOrigin(xy_arr[0],xy_arr[1],xy_arr[2],xy_arr[3],xy_arr[4],xy_arr[5])
print count





