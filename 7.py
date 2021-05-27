# 7 10001st prime
import math
import itertools
def is_prime(n):
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n % i == 0:
            return False
        else:
            continue
    return True
p = 0
for x in itertools.count(1):
    if is_prime(x):
        if p == 10001:
            print(x)
            break
        p += 1