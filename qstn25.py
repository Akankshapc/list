#25Q

elements=[23,14,56,12,19,9,15,25,31,42,43]
b=len(elements)
even=0
odd=0
index=0
while index<b:
	if elements[index]%2==0:
		even+=1
	else:
		odd+=1
	index+=1
print('total even nmbr:',even)
print('total odd nmbr:',odd)
