# problem 55
# time complexity: O(C(50) * n), = O(n) n is number of numbers considered
def is_palindrome(n):
	orig_n = n
	n_str = str(n)
	n_rev = int(n_str[::-1])
	for i in range(50):
		sum = n_rev + n
		if str(sum) == str(sum)[::-1]:
			print str(orig_n)+ " is palindromic!"
			return True
		n = sum
		n_rev = int(str(n)[::-1])
	return False
	
count = 0
for i in range(1,10000):
	if not is_palindrome(i):
		count += 1
		
print count
		
