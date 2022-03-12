#even nmbrs & odd nmbrs #

x=[9,18,15,13,28,45,49,95,22,24]
i=0
a=[]
b=[]
while i<len(x):
	if x[i]%2==0:
		a.append(x[i])
	else:
		b.append(x[i])
	i+=1
print("even nbr",a)
print("odd nbr",b)
