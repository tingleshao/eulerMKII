mat_file = open('matrix.txt','r')
mat_lst = mat_file.read().split('\n')[:-1]
mat = []
for line in mat_lst:
	mat.append(map(int,line.split(',')))

#mat = [[31,673,234,103,18],[201,86,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
firstline = [mat[0][0]]
for i in range(1,80):
	firstline.append(mat[0][i]+firstline[i-1])
opt_val = [firstline,[]]
#for i in range(80):
#	optimal_value.append([]*80)

for i in range(1,80):
	for j in range(80):
		if j == 0:
			opt_val[i].append(opt_val[i-1][j]+mat[i][j])
		else:
			opt_val[i].append(min(opt_val[i-1][j],opt_val[i][j-1])+mat[i][j])
	opt_val.append([])
print len(opt_val)
print opt_val
			

