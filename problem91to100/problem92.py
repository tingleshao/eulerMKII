# problem 92
count = 0

def square(n):
	return n * n 

for i in range(1,10000000):
	j = i
	while True:
		if j == 1:
			break
		if j == 89:
			count += 1 
			print i
			break
		j_lst = map(square, map(int, list(str(j))))
		j = 0
		for d in j_lst:
			j += d 
print count
