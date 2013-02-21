# prob 18
# precompute the sums between each layer
tri = [[75]]
tri.append( [95,64] )
tri.append( [17,47,82] )
tri.append( [18,35,87,10] )
tri.append( [20,4,82,47,65] )
tri.append( [19,1,23,75,3,34] )
tri.append( [88,2,77,73,7,63,67] )
tri.append( [99,65,4,28,6,16,70,92] )
tri.append( [41,41,25,56,83,40,80,70,33] )
tri.append( [41,48,72,33,47,32,37,16,94,29])
tri.append( [53,71,44,65,25,43,91,52,97,51,14] )
tri.append( [70,11,33,28,77,73,17,78,39,68,17,57] )
tri.append( [91,71,52,38,17,14,91,43,58,50,27,29,48] )
tri.append( [63,66,4,68,89,53,67,30,73,16,69,87,40,31] )
tri.append( [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23] )

for i in range(1,15):
	for j in range(len(tri[i])):
		if j == 0:
			tri[i][j] = tri[i-1][j] + tri[i][j]
		elif j == len(tri[i]) - 1:
			tri[i][j] = tri[i-1][j-1] + tri[i][j]
		else:
			tri[i][j] = max([tri[i][j]+tri[i-1][j],tri[i][j]+tri[i-1][j-1]])

for row in tri:
	print row
	