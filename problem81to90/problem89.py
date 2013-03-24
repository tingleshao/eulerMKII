# problem 89
roman_file = open('roman.txt','r')
roman_lst = roman_file.read().strip().split('\n')
for r in roman_lst:
	print r
print len(roman_lst)

roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def conv_roman_to_int(roman):
	roman_len = len(roman)
	val  = 0
	i = 0
	while i < roman_len-1:
		if roman_dict[roman[i]] < roman_dict[roman[i+1]]:
			val = val + (roman_dict[roman[i+1]] - roman_dict[roman[i]])
			i = i + 2
		else:
			val = val + (roman_dict[roman[i]])
			i = i + 1
	if i == roman_len-1:
		val = val + roman_dict[roman[i]]
	return val


def conv_int_to_minimal_roman(n):
	str_n = str(n)
	len_d = len(str_n)
	roman = ""
	if len_d >= 4:
		roman = roman + 'M' * int(str_n[:-3])
	if len_d >= 3:	
		str_n_last_3 = str_n[-3:-2]
		if str_n_last_3 == '9':
			roman = roman + 'CM'
		elif str_n_last_3 == '8':
			roman = roman + 'DCCC'
		elif str_n_last_3 == '7':
			roman = roman + 'DCC'
		elif str_n_last_3 == '6':
			roman = roman + 'DC'
		elif str_n_last_3 == '5':
			roman = roman + 'D'
		elif str_n_last_3 == '4':
			roman = roman + 'CD'
		elif str_n_last_3 == '3':
			roman = roman + 'CCC'
		elif str_n_last_3 == '2':
			roman = roman + 'CC'
		elif str_n_last_3 == '1':
			roman = roman + 'C'
	if len_d >= 2:
		str_n_last_2 = str_n[-2:-1]
		if str_n_last_2 == '9':
			roman = roman + 'XC'
		elif str_n_last_2 == '8':
			roman = roman + 'LXXX'
		elif str_n_last_2 == '7':
			roman = roman + 'LXX'
		elif str_n_last_2 == '6':
			roman = roman + 'LX'
		elif str_n_last_2 == '5':
			roman = roman + 'L'
		elif str_n_last_2 == '4':
			roman = roman + 'XL'
		elif str_n_last_2 == '3':
			roman = roman + 'XXX'
		elif str_n_last_2 == '2':
			roman = roman + 'XX'
		elif str_n_last_2 == '1':
			roman = roman + 'X'
	str_n_last_1 = str_n[-1]
	if str_n_last_1 == '9':
		roman = roman + 'IX'
	elif str_n_last_1 == '8':
		roman = roman + 'VIII'
	elif str_n_last_1 == '7':
		roman = roman + 'VII'
	elif str_n_last_1 == '6':
		roman = roman + 'VI'
	elif str_n_last_1 == '5':
		roman = roman + 'V'
	elif str_n_last_1 == '4':
		roman = roman + 'IV'
	elif str_n_last_1 == '3':
		roman = roman + 'III'
	elif str_n_last_1 == '2':
		roman = roman + 'II'
	elif str_n_last_1 == '1':
		roman = roman + 'I'
	return roman

saved = 0
for roman in roman_lst:
	len_roman = len(roman)	
	new_roman =  conv_int_to_minimal_roman(conv_roman_to_int(roman))
	print "roman: " + roman
	print "new_roman: " + new_roman
	len_new_roman = len(new_roman)
	if len_new_roman > len_roman:
		print "error: new roman length larger than roman length: " + roman
		break
	if conv_roman_to_int(new_roman) != conv_roman_to_int(roman):
		print "error at roman: " + roman + "\nnew roman value: " + str(conv_roman_to_int(new_roman)) + "\nold roman value: " +  str(conv_roman_to_int(roman))
		break
	print "roman length: " + str(len_roman)
	print "new roman length : " + str(len_new_roman)
	saved += len_roman - len_new_roman
	print "---------"


print saved
