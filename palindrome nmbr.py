#palindrome 
a=input('entr string:')
b=a[-1::-1]
if a==b:
	print(a,'palindrome ')
else:
	print(a,'not palindrome ')
