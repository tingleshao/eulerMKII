# problem 29
# straight forward solution
terms = []
for i in range(2,101):
	for j in range(2,101):
		term = i ** j 
		if term not in terms:
			terms.append(term)

print len(terms)
