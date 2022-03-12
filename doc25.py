t= [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
a=[]
c=0
while i<len(t):
	j=0
	b=[]
	c=0
	while j<=i:
		if t[i] ==t[j]:
			c=c+1
		
		j=j+1
	if c>3:
		#b.append(t[i])
		#b.append(c)
		#if b not in t:
		a.append(t[i])
	i=i+1
print(a)
