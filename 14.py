
def collatz(n):
 counter = 1
 while n>1:
  if n%2 == 0:
   n = n/2
   counter += 1
  else:
   n = 3*n+1
   counter += 1
  if n == 1:
   return counter

largest_number = 0

large_seq = 0

for i in range(1000000,1,-1):

 n = collatz(i)

 if n > large_seq:
  largest_number = i
  large_seq = n

print (largest_number)
