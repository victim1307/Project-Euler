def larrgestPalindrome(n):

	upper_limit = (10**(n))-1
	lower_limit = 1 + upper_limit//10
	max_product = 0
	for i in range(upper_limit,lower_limit-1, -1):
	
		for j in range(i,lower_limit-1,-1):
			product = i * j
			if (product < max_product):
				break
			number = product
			reverse = 0
			while (number != 0):
			
				reverse = reverse * 10 + number % 10
				number =number // 10
			if (product == reverse and product > max_product):
				max_product = product
	return max_product
n = 3
print(larrgestPalindrome(n))
