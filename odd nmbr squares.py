#finding squares of odd numbers
a=[1,2,3,4,5,6,7,8,9]
i=0
b=[ ]
while i<len(a):
	if a[i]%2!=0:
		p=a[i]**2
		b.append(p)
	i+=1
print(b)
