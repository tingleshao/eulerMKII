trif = open('triangle.txt')
tri = []
line = trif.readline()
while line:
	tri.append(map(int,line.split(' ')))
	line = trif.readline()
	
for row in tri:
	print row
	
for i in range(1,100):
	for j in range(len(tri[i])):
		if j == 0:
			tri[i][j] = tri[i-1][j] + tri[i][j]
		elif j == len(tri[i]) - 1:
			tri[i][j] = tri[i-1][j-1] + tri[i][j]
		else:
			tri[i][j] = max([tri[i][j]+tri[i-1][j],tri[i][j]+tri[i-1][j-1]])

for row in tri:
	print max(row)
	
