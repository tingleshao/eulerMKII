# problem 213
# http://projecteuler.net/thread=213
#First? I just calculated the probability of each flee being in each square after 50 rounds, and #summed the probability of each square being empty based on those probabilities. Runs in a little #under 4 seconds on my machine.
'''import random

trials = 10001
totalcount = 0
for k in range(trials):
	
	grid = []
	for i in range(30):
		row = []
		for j in range(30):
			row.append(1)
		grid.append(row)
	bells = 50
	for i in range(bells):
		for row in range(30):
			for col in range(30):
				ran = random.random()
				grid[row][col] -=1
				if row == 0:
					if col == 0:
						if ran < 1.0 / 2:
							grid[row+1][col] += 1
						else:
							grid[row][col+1] += 1
					if col == 29:
						if ran < 1.0 / 2:
							grid[row+1][col] += 1
						else:
							grid[row][col-1] += 1
					else:
						if ran < 1.0 / 3:
							grid[row][col+1] += 1
						elif ran < 2.0 /3:
							grid[row][col-1] += 1	
						else:
							grid[row+1][col] += 1
				elif row == 29:
					if col == 0:
						if ran < 1.0 / 2:
							grid[row-1][col] += 1
						else:
							grid[row][col+1] += 1
					if col == 29:
						if ran < 1.0 / 2:
							grid[row-1][col] += 1
						else:
							grid[row][col-1] += 1
					else:
						if ran < 1.0 / 3:
							grid[row][col-1] += 1
						elif ran < 2.0 /3:
							grid[row][col+1] += 1	
						else:
							grid[row-1][col] += 1
				else:
					if col == 0:
						if ran < 1.0 / 3:
							grid[row-1][col] += 1
						elif ran < 2.0 / 3:
							grid[row][col+1] += 1
						else: 
							grid[row+1][col] += 1
					if col == 29:
						if ran < 1.0 / 3:
							grid[row-1][col] += 1
						elif ran < 2.0 / 3:
							grid[row][col-1] += 1
						else: 
							grid[row+1][col] += 1
					else:
						if ran < 1.0 / 4:
							grid[row][col-1] += 1
						elif ran < 2.0 /4:
							grid[row-1][col] += 1	
						elif ran < 3.0 /4:
							grid[row][col+1] += 1
						else:	
							grid[row+1][col] += 1
	count = 0

	for i in range(30):
		for j in range(30):
			if grid[i][j] == 0:
				count += 1

	print count
	totalcount += count
print float(totalcount ) / trials'''

# ---
grid = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for i in range(900):
	mat0 = []
	mat1 = []
	for j in range(30):
		row0 = []
		row1 = []
		for k in range(30):
			row0.append(0.0)
			row1.append(0.0)
		mat0.append(row0)
		mat1.append(row1)
	grid.append([mat0,mat1])
for f in range(900):
	print f
	grid[f][0][f%30][f/30] = 1.0;
	for r in range(1,51):
		cur = r % 2
		prev = 1 - cur
		newmat = []
		for j in range(30):
			row = []
			for k in range(30):
				row.append(0.0)
			newmat.append(row)
      		grid[f][cur] = newmat
		for x in range(30):
			for y in range(30):
				tot = 4
				if x == 0 or x == 29:
					tot -= 1
				if y == 0 or y == 29:
					tot -= 1 
				for d in range(4):
					nx = x + dx[d]
					ny = y + dy[d]
					if nx < 0 or ny < 0 or nx >= 30 or ny >= 30:
						continue
					#print grid[f][prev][x][y] / float(tot)
					grid[f][cur][nx][ny]  += grid[f][prev][x][y] / float(tot)
ret = 0.0
for x in range(30):
	for y in range(30):
		p = 1.0
		for f in range(900):
			p *= 1 - grid[f][0][x][y]
		print p
		ret += p


print ret
