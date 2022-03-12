#KBC #
a=['how many continents are there?','what is capital of india?','which course availbe in NG?']
b=[['four','nine','seven','eight'],['chandigarh','bhopal','chennai','delhi'],['software','concelling','tourism']]
c=[3,4,1]
i=0
count=0
while i<len(a):
    print(' your',i+1,'question')
    print(i+1,a[i])
    print('select options')
    j=0
    while j<len(b[i]):
        print(j+1,b[i][j])
        j=j+1
    n=int(input('entr ur option'))
    if n==c[i]:
        print('congratulations....')
    else:
         print('wrong answer')
         break
    i=i+1
print('game over')

