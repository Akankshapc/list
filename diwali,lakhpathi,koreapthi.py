a=[3000,600000,324990909,30000,5600000,690909090,3101010,510,4100]
i=0
b=0
c=0
d=0
e=0
while i<len(a):
	if a[i]>100 and a[i]<100000:
		c+=1
	elif a[i]>100000 and a[i]<10000000:
		d+=1
	elif a[i]>10000000 and a[i]<1000000000:
		e+=1
	i+=1
print("diwale",c)
print("lakhpati",d)
print("corepati",e)


