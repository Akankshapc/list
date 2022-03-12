##average of all marks
a= [
[78,76,94,86,88],
[91,71,98,65,],
[95,45,78,],
[87,67,49,68,88]
]
i=0
b=len(a[0])
c=len(a[1])
d=len(a[2])
e=len(a[3])
while i<len(a):
	
	j=0
	sum=0
	
	while j<len(a[0]):
		sum=sum+a[0][j]
		k=0
		sum1=0
		while k<len(a[1]):
			sum1=sum1+a[1][k]
			k=k+1
			s=0
			sum2=0
			while s<len(a[2]):
				sum2=sum2+a[2][s]
				s=s+1
				l=0
				sum3=0
				while l<len(a[3]):
					sum3=sum3+a[3][l]
					l=l+1
				
		j=j+1
	i=i+1
print(sum)
print(sum1)
print(sum2)
print(sum3)
print('av',sum/b)
print('av1',sum1/c)
print('av2',sum2/d)
