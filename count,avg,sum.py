##use,count,avg,sum
a=[23,14,56,12,19,9,15,25,31,42,43]
even=[ ]
odd=[ ]
for nbr in a:
	if nbr%2==0:
		even.append(nbr)
	else:
		odd.append(nbr)
print('count of even nbr:',even)
print('count of odd nbrs:',odd)
print('sum of even nbr:',sum(even))
print('sum of odd nbrs:',sum(odd))
print('avg of even nbr:',sum(even)//len(even))
print('avg of odd nbr: ',sum(odd)//len(odd))
print('avrge of total:',sum(a)//len(a))
print('total sum of all nbrs:',sum(a))
print('count of all nbrs:',len(a))
