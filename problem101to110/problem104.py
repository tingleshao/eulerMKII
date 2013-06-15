def fast_fibo(n):
	return fast_fib_n(1,1,n)

def fast_fib_n(a,b,n):
	for i in xrange(n-1):
		temp = b
		b = a + b	
		a = temp
	return a 		
	

print fast_fibo(1)
print fast_fibo(2)
print fast_fibo(3)
print fast_fibo(2000)

start = fast_fibo(329466)
start2 = fast_fibo(329467)
for i in xrange(329466,329470):
	new_fib = start
	str_fib = str(new_fib)
	first_nine_list = list(str_fib[0:9])
	last_nine_list = list(str_fib[-9:])
	first_nine_list.sort()
	last_nine_list.sort()
	first_nine = "".join(first_nine_list)
	last_nine  = "".join(last_nine_list)
	print i 
	if first_nine == last_nine == "123456789":
		print "=============="
		print i
		break
	temp = start2
	start2 = start+ start2
	start = temp
