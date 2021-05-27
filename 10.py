import math
# Python program to display all the prime numbers within an interval
lower = 2
upper = 2000000
summ=0
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2,(int)(math.sqrt(num))+1):
           if (num % i) == 0:
               break
       else:
           summ+=num
print(summ)