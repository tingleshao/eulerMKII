# problem 46.py
# straight forward python implementation solution, runs < 5s
import math
prime_file = open('millionprimes.txt', 'r')
prime_lst_str  = prime_file.readline()
prime_lst = map(int, prime_lst_str.strip('[]').split(", "))
prime_lst.insert(0,2)
print "start"
for i in range(4,10000):
	if i % 2 == 1:
		if i not in prime_lst:
			print "i is composite number"
			flag = True
			for j in prime_lst:
				if j >= i:
					break
				p = j
				diff_div2 = (i - p) / 2
				if math.sqrt(diff_div2) % 1 == 0:
					print "not this: " + str(i)
					flag = False
					break
			if flag:
				print "find ONe!"
				print "p: "  + str(i)
				break