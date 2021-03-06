# problem 243
#http://blog.dreamshire.com/2012/12/19/project-euler-problem-243-solution/
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ratio = 15499/94744.0
 
def denom(ratio):
  d, s = 1, 1
  for p in primes:
    d *= p
    s *= p-1
    for i in range(2, p):
      if s*i / (d*i-1.) < ratio:
        return d*i
  return "Please buy more primes!"
 
print 'Answer to PE243 = ',denom(ratio)
