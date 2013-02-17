# project euler problem 4
a = 999
b = 999
plst = []
for i in range(900):
	a = 999-i
	for j in range(999):
		b = 999-j
		p = a * b
		pstr = str(p)
		pstr_inv = pstr[::-1]
		if pstr_inv == pstr:
			plst.append(p)
		
			
print max(plst)
			