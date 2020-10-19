from functools import *
numbers=[1,2,3,4,5,6]

#finding square of numbers

squaredata=list(map(squares,numbers))
print(squaredata)

#find cube of numbers

cubedata=list(map(cubes,numbers))
print(cubedata)

#filter even numbers from list

def evennumbers(num):
    if num%2 ==0:
        return num
evens=list(filter(evennumbers,numbers))
print(evens)

#square method using lambda funtion

squaredata=list(filter(lambda num:num%2==0,numbers))
print(squaredata)

#convert all the elemnts into upper case
names=["kkk","hgf","gfj"]

upp=list(map(lambda items:items.upper(),names))
print(upp)

#finding maximum of the elements of the list

#numbers=[2,1,4,3]
max=reduce(lambda num1,num2:num1 if num1>num2 else num2,numbers)
print(max)

#fi
nd total of elemnts in the list
total=reduce(lambda num1,num2:num1+num2,numbers)
print("sum of elements:",total)

#print all the possible pairs from the two lists
list1=[1,2,3]
list2=[4,5,6]

newlist=[]

for i in list1:
    for j in list2:
        newlist.append((i,j))
#print(newlist)

#above code using list comprehension
output=[(i,j) for i in list1 for j in list2]
#print(output)

#square of items of list1 using list comprehension
squares=[i*i for i in list1]
print(squares)

#OR
sq=[i**2 for i in list2] #square
print(sq)

#fetch even  numbers from list2
even=[i for i in list2 if i % 2 == 0]
print(even)

#print i- if i<5 and print
lst=[2,5,4,6,7,3,1,8]
output=[i+1 if i > 5 else i-1 for i in lst]
print(output)





