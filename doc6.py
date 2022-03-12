#multiplying 2numbers to get output

a=[1,2,3,4,5,6,7,8,9,10]
i=0
b=[]
while i<len(a):
	c=a[i]*a[i+1]
	b.append(c)
	i=i+2
print(b)
