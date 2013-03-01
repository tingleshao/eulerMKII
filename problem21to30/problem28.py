# problem 28
# 1001 by 1001: there will be 500 layers
sum = 1
curr= 3
diff = 2
for i in range(500):
	for j in range(4):
		sum = sum + curr
		curr = curr + diff
	curr = curr + 2
	diff = diff + 2

print sum
