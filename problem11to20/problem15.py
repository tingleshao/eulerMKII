#project euler problem 15
# pascal's triangle
def p(r,c):
	if r == 0 or c == 0:
		return 1
	else:
		return p(r,c-1) * (r+1-c) / c

for r in range(41):
	row = []
	for c in range(r+1):
		row.append(p(r,c))
	print row
	
print  p(40,20)