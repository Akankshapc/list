a=[[1,2,3],[4,5,6],[7,8,9]]
x=[]
i=0
while i<len(a):
	j=0
	b=[]
	while j<len(a):
		b.append(a[j][i])
		j+=1
	x.append(b)
	i+=1
print(x)
