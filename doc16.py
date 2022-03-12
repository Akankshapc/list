
a=[2,4,6,8]
i=1
b=[]
while i<len(a):
	p=a[-i]-a[-i-1]
	b.append(p)
	i=i+1
print(b)
