# problem 206
i = 1009950493
while True:
	
	print i 
	isq = str(i ** 2)
	if len(isq) == 19:
		if isq[0] == '1':
			if isq[2] == '2':
				if isq[4] == '3':
					if isq[6] == '4':
						if isq[8] == '5':
							if isq[10] == '6':
								if isq[12] == '7':
									if isq[14] == '8':
										if isq[16] == '9':
											if isq[18] == '0':
												print "-----------"
												print i
												print isq
												break
	i += 1
	if i == 1389026623:
		break
	
