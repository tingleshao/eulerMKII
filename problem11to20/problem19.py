# problem 19
# very straight forward solution
NUM_OF_MONTHS = 12
NUM_OF_YEARS = 100
cal = ""
for i in range(10000):
	cal = cal + "MTWHFSU"
cal_ind = 0
sum = 0
for i in range(NUM_OF_YEARS):
	year = 1900+i
	DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
	if year != 1900 and year % 4 == 0:
		DAYS[1] = 29
	for j in range(NUM_OF_MONTHS):
		cal_ind = cal_ind + DAYS[j]
		if cal[cal_ind] == 'S':
			sum = sum + 1
			
print sum