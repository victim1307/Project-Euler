a=1
b=1
c=1
for c in range(1,1000):
	for a in range(1,c):
		for b in range(1,a):
			if ((a**2)+(b**2))==(c**2):
				if (a+b+c)==1000:
					print(a*b*c)