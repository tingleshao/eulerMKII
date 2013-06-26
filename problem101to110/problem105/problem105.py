# problem 105

def is_special(A):
# for a set a, compute all possible sum
   sums = []
   sums_and_sizes = []
   len_A = len(A)
   sums = sum_sub_sets(A)
      
   for i in xrange(len(sums_and_sizes)-1):
      ii = sums_and_sizes[i]
      for j in xrange(i+1, len(sums_and_sizes)):
          jj = sums_and_sizes[j]
          if (ii[0] == jj[0]):
	       print "rule1"
               return False
	  if (ii[0] < jj[0] and ii[1] > jj[1]):
               print "rule2"
               return False
          if (ii[0] > jj[0] and ii[1] < jj[1]):
               print "rule2"
               return False
   return True

def plus_x(x):
    return lambda t : x + t

def sum_sub_sets(A):
    if len(A) == 0:
        return A
    else: 
        sums = []
        for i in xrange(len(A)):
           pick = A[i]
           sub = A[0:i] + A[i+1:]
           sub_sums = sum_sub_sets(sub)
          
           sums = map(plus_x(pick),sub_sums) + sub_sums
        print sums
        return sums

set_file = open('sets.txt', 'r')
list_of_sets = []

total_special_sum = 0
line = set_file.readline()
while(line):
    current_set = map(int,line.strip().split(','))
    if is_special(current_set):
	  total_special_sum += sum(current_set) 
          print str(current_set) + " is special!" 
          print "current sum: " + str(total_special_sum)
    line = set_file.readline()

print total_special_sum
