# problem 99
exp_file = open('base_exp.txt','r')
exps = exp_file.read().strip().split('\n')
base_lst = []
exp_lst = []
for e in exps:
	base = int(e.split(',')[0])
	exp = int(e.split(',')[1])
	base_lst.append(base)
	exp_lst.append(exp)

max_exp = 0
max_line = 1
ind = 0
for b in base_lst:
	print ind
	
	curr_x = int(str(b)[0] + '0' * len(str(b))) ** exp_lst[ind]
	if curr_x > max_exp: 
		print "aa"
		curr =  b ** exp_lst[ind]
		if curr > max_exp:
			max_exp = curr
			max_line = ind + 1
			print "line " + str(max_line) + " has max" 
		ind += 1
print "max: " + str(max_line)
			 
		
