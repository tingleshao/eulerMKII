# problem 40
# staright forward solution won't take so long
irrational = ""
for i in range(1,400000):
	if len(irrational) <= 1000000:
		irrational = irrational + str(i)
print len(irrational)
print irrational[11]
print int(irrational[0]) * int(irrational[9]) * int(irrational[99]) * int(irrational[999]) * int(irrational[9999]) * int(irrational[99999]) * int(irrational[999999])