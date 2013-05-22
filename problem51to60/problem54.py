# question B2

from sys import argv
SUIT = ['D','C','H','S']
#SUIT = ['S','H','C','D']
def convert_to_digit(x):
	if x.isdigit():
		return int(x)
	if x == "T":
		return 10
	if x == "J":
		return 11
	if x == "Q":
		return 12
	if x == "K":
		return 13
	if x == "A":
		return 14
		
def compare(x, y):
		if x[0].isdigit():
			if y[0].isdigit():
				if less_than(x, y):
					return -1
				elif less_than(y, x):
					return 1
				else:
					return compare_suit(x[1],y[1])
			else:
				return -1
		else:
			if y[0].isdigit():
				return 1
			else:
				if less_than(convert_to_digit(x),convert_to_digit(y)):
					return -1
				elif less_than(convert_to_digit(y), convert_to_digit(x)):
					return 1
				else:
					return compareSuit(x[1],y[1])
			
def compare_suit(x, y):
	if x == y:
		return 0
	else:
		return compare(SUIT.index(x), SUIT.index(y))
			
def does_player_one_win(p1, p2):
	if (is_royal_flush(p1) != is_royal_flush(p2)):
		return is_royal_flush(p1) > is_royal_flush(p2)
	if is_straight_flush(p1) != is_straight_flush(p2):
		return is_straight_flush(p1) > is_straight_flush(p2)
	if is_four_of_a_kind(p1) != is_four_of_a_kind(p2): 
		return is_four_of_a_kind(p1) > is_four_of_a_kind(p2)
	if is_full_house(p1, 1) != is_full_house(p2, 1):
		return is_full_house(p1, 1) > is_full_house(p2, 1)
	if is_full_house(p1, 2) != is_full_house(p2, 2):
		return is_full_house(p1, 2) < is_full_house(p2, 2)
	if is_straight(p1) != is_straight(p2):
		return is_straight(p1) > is_straight(p2)
	if is_three_of_a_kind(p1) != is_three_of_a_kind(p2):
		return  is_three_of_a_kind(p1) > is_three_of_a_kind(p2)
	if is_two_pairs(p1,1) != is_two_pairs(p2,1):
		return is_two_pairs(p1,1) > is_two_pairs(p2,1)
	if is_two_pairs(p1,2) != is_two_pairs(p2,2):
		return is_two_pairs(p1,2) > is_two_pairs(p2,2)
	if is_one_pair(p1) != is_one_pair(p2):
		return is_one_pair(p1) > is_one_pair(p2)
	if is_high_card(p1,0) != is_high_card(p2,0):
		return is_high_card(p1,0) > is_high_card(p2,0)
	if is_high_card(p1,1) != is_high_card(p2,1):
		return is_high_card(p1,1) > is_high_card(p2,1)
	if is_high_card(p1,2) != is_high_card(p2,2):
		return is_high_card(p1,2) > is_high_card(p2,2)
	if is_high_card(p1,3) != is_high_card(p2,3):
		return is_high_card(p1,3) > is_high_card(p2,3)
	return False
	
def is_straight(p):
	for i in range(4):
		if convert_to_digit(p[i][0]) != convert_to_digit(p[i+1][0]) - 1:
			return -1
	return convert_to_digit(p[4][0])
	return -1
		
def is_flush(p): 
	for i in range(4):
		if p[i][1] != p[i+1][1]:	
			return -1
	return convert_to_digit(p[4][0])
	return -1
	
def is_straight_flush(p):
	if (is_flush(p) > 0 and is_straight(p) > 0):
		return convert_to_digit(p[4][0])
	return -1
	
def is_royal_flush(p):
	if is_flush(p) == 14:
		return 14
	return -1
		
def is_four_of_a_kind(p):
	if convert_to_digit(p[0][0]) == convert_to_digit(p[1][0]) ==  convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]):
		return convert_to_digit(p[0][0])
	if convert_to_digit(p[1][0]) == convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]) == convert_to_digit(p[4][0]):
		return convert_to_digit(p[1][0])
	return -1

def is_full_house(p, set):
	if set == 1 and  (convert_to_digit(p[0][0]) == convert_to_digit(p[1][0]) == convert_to_digit(p[2][0])) and (convert_to_digit(p[3][0]) == convert_to_digit(p[4][0])):
		return convert_to_digit(p[0][0])
	if set == 2 and  (convert_to_digit(p[0][0]) == convert_to_digit(p[1][0]) == convert_to_digit(p[2][0])) and (convert_to_digit(p[3][0]) == convert_to_digit(p[4][0])):
		return convert_to_digit(p[4][0])
	if set == 1 and  (convert_to_digit(p[0][0]) == convert_to_digit(p[1][0])) and (convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]) == convert_to_digit(p[4][0])):
		return convert_to_digit(p[4][0])
	if set == 2 and  (convert_to_digit(p[0][0]) == convert_to_digit(p[1][0])) and (convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]) == convert_to_digit(p[4][0])):
		return convert_to_digit(p[0][0])
	return -1
	
def is_three_of_a_kind(p):
	if convert_to_digit(p[0][0]) == convert_to_digit(p[1][0]) == convert_to_digit(p[2][0]):
		return convert_to_digit(p[0][0])
	if convert_to_digit(p[1][0]) == convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]):
		return convert_to_digit(p[1][0])
	if convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]) == convert_to_digit(p[4][0]):
		return convert_to_digit(p[2][0])
	return -1
	
def is_two_pairs(p, set):
	if set == 1 and convert_to_digit(p[0][0]) == convert_to_digit(p[1][0])  and convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]):
		return convert_to_digit(p[0][0]) 
	if set == 2 and convert_to_digit(p[0][0]) == convert_to_digit(p[1][0])  and convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]):
		return convert_to_digit(p[2][0]) 
	if set == 1 and convert_to_digit(p[0][0]) == convert_to_digit(p[1][0])  and convert_to_digit(p[3][0]) == convert_to_digit(p[4][0]):
		return convert_to_digit(p[0][0]) 
	if set == 2 and convert_to_digit(p[0][0]) == convert_to_digit(p[1][0])  and convert_to_digit(p[3][0]) == convert_to_digit(p[4][0]):
		return convert_to_digit(p[3][0]) 
	if set == 1 and convert_to_digit(p[1][0]) == convert_to_digit(p[2][0])  and convert_to_digit(p[3][0]) == convert_to_digit(p[4][0]):
		return convert_to_digit(p[1][0]) 
	if set == 2 and convert_to_digit(p[1][0]) == convert_to_digit(p[2][0])  and convert_to_digit(p[3][0]) == convert_to_digit(p[4][0]):
		return convert_to_digit(p[3][0]) 
	return -1
		
def is_one_pair(p):
	if convert_to_digit(p[0][0]) == convert_to_digit(p[1][0]):
		return convert_to_digit(p[0][0])
	if convert_to_digit(p[1][0]) == convert_to_digit(p[2][0]):
		return convert_to_digit(p[1][0])
	if convert_to_digit(p[2][0]) == convert_to_digit(p[3][0]):
		return convert_to_digit(p[2][0])
	if convert_to_digit(p[3][0]) == convert_to_digit(p[4][0]):
		return convert_to_digit(p[3][0])
	return -1

def is_high_card(p, card):
	return convert_to_digit(p[4-card][0])
	#return -1
	
	
def get_card_val(x):
	return convert_to_digit(x[0]) + SUIT.index(x[1])
		
def compare_card(x,y):
	return get_card_val(x) - get_card_val(y)
	
pokers = open('poker.txt','r')
plays = []
for i in range(1000):
	one_play_str_lst = pokers.readline().strip().split(' ')
	player_one = []
	player_two = []
	for k in range(5):
		player_one.append(one_play_str_lst[k])
		player_two.append(one_play_str_lst[5+k])
	player_one.sort(compare_card)
	player_two.sort(compare_card)
	plays.append([player_one,player_two])
	
count = 0
for line in plays:
	#print line
	if does_player_one_win(line[0],line[1]):
		count += 1
print count 

# answer: 383
