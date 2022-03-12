n=input("enter parenthesis")
i=0
c1=0
c2=0
while i<len(n):
	if n[i]=='(':
		c1=c1+1
	elif n[i]==')':
		c2=c2+1
	i+=1
if c1==c2:
	print('valid')
else:
	print('invalid')
