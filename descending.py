#descending order##

list=[2,5,1,0,9,6]
n=len(list)
i=0
while i<n-1:
	j=0
	while j<n-1:
		if list[j]<list[j+1]:
			list[j],list[j+1]=list[j+1],list[j]
		j+=1
	i+=1
print(list)
	