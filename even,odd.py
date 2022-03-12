#even 0
#odd 1
x=[1,2,3,4,5,6,7,8,9,10]
i=0
a=[]
b=[]
while i<len(x):
	if x[i]%2==0:
		a.append(0)
	else:
		b.append(1)
	i+=1
print(a)
print(b)
