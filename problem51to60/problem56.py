# problem 56
# running this code costs 1 sec. 
max_sum = 0 
for a in range(1,101):
	for b in range(1,101):
		apb = a ** b
		apb_digit_lst = list(str(apb))
		sum = 0 
		for d in apb_digit_lst:
			sum = sum + int(d)
		if sum > max_sum:
			max_sum = sum
			
print max_sum