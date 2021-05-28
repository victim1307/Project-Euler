lst2=[]
d=0
for x in range(1,10000):
	lst=[]
	lst1=[]
	a=0
	b=0
	for i in range(1,x):
		if x%i==0:
			lst.append(i)
	for j in range(len(lst)):
		a=a+lst[j]
	for k in range(1,a):
		if a%k==0:
			lst1.append(k)
	for l in range(len(lst1)):
		b=b+lst1[l]
	if(x==b and a!=b):
		lst2.append(x)
for y in range(len(lst2)):
	d+=lst2[y]
print(d)