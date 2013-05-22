# problem 166

def get_new_grid():
	grid = []
	for j in range(4):
		row = []
		for k in range(4):
			row.append(0)
		grid.append(row)
	return grid

for i in range(37):
	sum_ = i
	grid = get_new_grid()
	for row in grid:
		for ele in row:
			for j in range(10):
				grid[row] = j
				if 

		
