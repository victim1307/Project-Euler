
# import math
# def lcm(n):
#     ans = 1
#     for i in range(1, n + 1):
#         ans = int((ans * i)/math.gcd(ans, i))        
#     return ans
# n = 20
# print (lcm(n))
import math
start = 2
end = 20
lst=[]
lst2=[]  
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        lst.append(i)
for i in lst:
	for j in range (1,10):
		if i**j>= end:
			lst2.append(i**(j-1))
			break
print(math.prod(lst2))