# question A1
# dynamic programming 
total = 200
currs = [1,2,5,10,20,50,100,200]
ways = []
for i in range(total+1):
	ways.append(0)
ways[0] = 1
	
for  i in range(8):
	for j in range(currs[i],total+1):
		ways[j] += ways[j-currs[i]]
		
print ways[-1]

# the answer is: 73682