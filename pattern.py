#pattern through list#

list1=[1,2,3,4,5,6]
list2=[2,3,1,0,7]
i=0
list=[]
while i<len(list1):
	if list1 not in list2:
		list.append(list1[i])
	i+=1
	print(list)
