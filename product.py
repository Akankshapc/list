##product
list=[3,6,9]
i=0
a=[ ]
p=1
while i<len(list):
	if list[i] not in a:
		a.append (list[i])
		p=p*list[i]
	i+=1
print(a)
print(p)
