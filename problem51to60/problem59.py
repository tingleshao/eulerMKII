# problem 59
# the key is god!!!!
from sys import argv
encyptd_file = open('cipher1.txt','r')
encyptd_str = encyptd_file.readline()
encyptd_lst = map(int, encyptd_str.strip('[]\n').split(",") )

letters = 'abcdefghijklmnopqrstuvwxyz'
text_len = len(encyptd_lst)

a = 'g'
b = 'o'
c = 'd'
key = [ord(a), ord(b), ord(c)]
decrept = ""
sum = 0
for i in range(text_len/3):
	decrept = decrept + chr(encyptd_lst[3*i] ^ key[0])
	decrept = decrept + chr(encyptd_lst[3*i+1] ^ key[1])
	decrept = decrept + chr(encyptd_lst[3*i+2] ^ key[2])
	
	sum = sum + (encyptd_lst[3*i] ^ key[0])
	sum = sum + (encyptd_lst[3*i+1] ^ key[1])
	sum = sum + (encyptd_lst[3*i+2] ^ key[2])
	print sum
sum  = sum + (encyptd_lst[-1] ^ key[0])
decrept = decrept + chr(encyptd_lst[-1] ^ key[0])
	
print decrept
print sum
print "-----------"
			
# g 
#  o
