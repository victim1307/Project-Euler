import math
def get_prime_factors(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i
    if number > 2:
        prime_factors.append(int(number))
    return prime_factors

for x in range(1,20000):
    y=(x*(x+1))/2
    lst2= get_prime_factors(y)
    #print(lst2)
    lst = get_prime_factors(y)
    lst=list(set(lst))
    a=1
    for x1 in lst:
        a=(lst2.count(x1)+1)*(a)

    if (a-1)>=500:
        print(y)
        break
            