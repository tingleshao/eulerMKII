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

# dynamic programming solution:
def dp(sze):
	grid = []
	for i in range(sze):
		row = []
		for j in range(sze):
			if i == 0 or j == 0:
				row.append(1)
			else:
				row.append(0)
		grid.append(row)
	for i in range(sze):
		for j in range(sze):
			if i > 0 and j > 0:
				grid[i][j] = grid[i-1][j] + grid[i][j-1]
	return grid
g = dp(21)
for row in g:
	print row