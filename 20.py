a=1
for i in range(1,101):
	a=a*i
a=[int(x) for x in str(a)]
b=0
for j in range(0,len(a)):
	b=b+a[j]
print(b)