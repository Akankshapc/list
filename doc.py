A=[1,2,3]
a=int(input("enter 1st nmbr"))
b=int(input("enter 2nd nmbr"))
c=int(input("enter 3rd nmbr"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
	for j in range(0,3):
		for k in range(0,3):
			if (i!=j&j!=k&k!=i):
				print(d[i],d[j],d[k])
