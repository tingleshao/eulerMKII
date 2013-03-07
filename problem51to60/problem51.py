# first try 1000 to 10000
# first prime >=1000: index 168, first >= 10000: index 1229
prime_file = open('millionprimes.txt', 'r')
prime_lst_str  = prime_file.readline()
prime_lst = map(int, prime_lst_str.strip('[]').split(", "))
prime_lst.insert(0,2)

# first process these primes, reduce them to the one with at least two same digits
ddl_prime_lst = []

def unique_lst(lst):
	u_lst = []
	for i in lst:
		if i not in u_lst:
			u_lst.append(i)
	return u_lst
for i in range(168,1229):
	p = prime_lst[i]
	if len(unique_lst(list(str(p)))) < len(str(p)):
		ddl_prime_lst.append(p)
#print ddl_prime_lst

# if the ddl_prime_lst has the replaceable number at the last digit, it should not be considered
# since it will be replaced by one of 2 and 5
def is_repeat_digit_index_at_lowest(p):
	str_p_lst = list(str(p))
	lowest = str_p_lst[-1]
	for i in str_p_lst[:-1]:
		if i == lowest and len(unique_lst(str_p_lst)) == len(str_p_lst)-1:
			return True
	return False

ddl_prime_lst2 = []
for p in ddl_prime_lst:
		if not is_repeat_digit_index_at_lowest(p):
			ddl_prime_lst2.append(p)
print ddl_prime_lst2

# work in the range 1000~10000
# first find the two repeat ones
ddl_prime_lst2_1 = []
for p in ddl_prime_lst2:
	str_p_lst = list(str(p))
	if len(unique_lst(str_p_lst)) == len(str_p_lst)-1:
			ddl_prime_lst2_1.append(p)
print ddl_prime_lst2_1

def find_repeat_index(p):
	p_str_lst = list(str(p))
	
	
	
	
for p in ddl_prime_lst2_1:

	for i in range(10):
		




'''
def common_with_other_two_same(lst1,lst2,lent):
	# extract common between two lists
	common = []
	lst1cp = []
	for i in lst1:
		lst1cp.append(i)
	lst2cp = []
	for i in lst2:
		lst2cp.append(i)
		
	for i in lst1cp:
		if i in lst2cp:
			common.append(i)
			lst2cp.remove(i)
		if len(common) == lent:
			break
	if lst2cp[1] != lst2cp[0]:
		return False
	for i in common:
		lst1cp.remove(i)
	if lst1cp[1] != lst2cp[0]:
		return False
	return True
	
def has_equal_in_place(strp1,strp2,num):
	

for i in range(168,1229):
	p = prime_lst[i]
	str_p = str(p)
	prime_car_lst = list(str_p)
	prime_car_lst.sort()
	sameLst = [p]
	for j in range(i+1,1229):
		p2 = prime_lst[j]
		str_p2 = str(p2)
		prime2_car_lst = list(str_p2)
		prime2_car_lst.sort()
		if common_with_other_two_same(prime_car_lst,prime2_car_lst,2):
			sameLst.append(p2)
	if len(sameLst) >= 8:
		print sameLst
'''			
		