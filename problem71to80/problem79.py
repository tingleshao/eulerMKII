# problem 79
key_file = open('keylog.txt','r')
key_lst = key_file.read().strip().split('\n')
for k in key_lst:
	print k
print len(key_lst)

#.... actually it can be solved using pencil/paper
