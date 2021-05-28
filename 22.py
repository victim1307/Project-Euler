f=open("names.txt","r")
lst=sorted([n.strip('"') for n in f.read().split(",")])
a=0
b=[]
c=0
for x in lst:
	res=list(x)
	for i in range(len(res)):
		a=a+(ord(res[i])-64)
	b.append(a)
	a=0
#print(b)
for i in range(len(b)):
	c=c+(b[i]*(i+1))
print(c)
