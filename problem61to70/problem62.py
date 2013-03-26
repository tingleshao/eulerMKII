# problem 62
# runs in ms.
cube_dict = {}
for i in range(10000):
	c = i ** 3
	print i
	lst_c = list(str(c))
	lst_c.sort()
	cc = ''.join(lst_c)
	if cube_dict.has_key(cc):
		cube_dict[cc].append(c)
	else:
		cube_dict[cc] = [c]
	if len(cube_dict[cc]) == 5:
		print "found one"
		print cube_dict[cc]
		break
	
	
