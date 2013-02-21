# pb 17
# this finally turns out to be wrong: 22024 ( the answer is 21124)
def	num_to_str(n):
	# assume n < 1000
	numstr = ""
	hund_digit = n / 100
	if hund_digit > 0:
		numstr  = numstr + digit_to_str(hund_digit) + ' hundered ' 
	remain = ( n % 100 ) 
	if hund_digit > 0 and remain > 0:
		numstr = numstr + ' and '
	if remain < 20 and remain > 9:
		numstr = numstr + teen_digit_to_str(remain)
	else:
		ten_digit = remain / 10
		if ten_digit > 0:
			numstr = numstr + ten_digit_to_str(ten_digit) + ' '
		lst_digit = remain % 10
		if lst_digit > 0:
			numstr = numstr + digit_to_str(lst_digit)
	return numstr
		
		
def digit_to_str(d):
	if d == 1:
		return 'one'
	elif d == 2:
		return 'two'
	elif d == 3:
		return 'three'
	elif d == 4:
		return 'four'
	elif d == 5:
		return 'five'
	elif d == 6:
		return 'six'
	elif d == 7:
		return 'seven'
	elif d == 8:
		return 'eight'
	else:
		return 'nine'
	
def ten_digit_to_str(d):
	if d == 2:
		return 'twenty'
	elif d == 3:
		return 'thirty'
	elif d == 4:
		return 'forty'
	elif d == 5:
		return 'fifty'
	elif d == 6:
		return 'sixty'
	elif d == 7:
		return 'seventy'
	elif d == 8:
		return 'eighty'
	else:
		return 'ninety'
		
def teen_digit_to_str(d):
	if d == 10:
		return 'ten'
	elif d == 11:
		return 'eleven'
	elif d == 12:
		return 'twelve'
	elif d == 13:
		return 'thirteen'
	elif d == 14:
		return 'fourteen'
	elif d == 15:
		return 'fifteen'
	elif d == 16:
		return 'sixteen'
	elif d == 17:
		return 'seventeen'
	elif d == 18:
		return 'eighteen'
	else:
		return 'nineteen'
	
		
#test
sum = 0
for i in range(6):
	print num_to_str(i)
	sum = sum + len(num_to_str(i).replace(" ", ""))
#sum = sum + len('onethousand')
print sum
	