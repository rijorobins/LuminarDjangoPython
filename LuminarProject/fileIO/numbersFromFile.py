#Print the numbers from file:numbers and find the sum ,minimum, and maximum numbers

f=open("numbers","r")

numbers=[]

for number in f:
    newnum=int(number.rstrip("\n"))
    #print(number)

    numbers.append(newnum)

print("Numbers are:",numbers)

print("sum of numbers in the list=",sum(numbers))

print("Maximum of numbers=",max(numbers))

print("Minimum of numbers=",min(numbers))

    #print(number)





















'''
f=open("numbers","r")
lst=[]
for i in f:
    numbers=int(i.rstrip("\n"))
    lst.append(numbers)
print(lst)

#Finding sum of elements in the list
sum=sum(lst)
print("Sum=",sum)

#Finding maximum value from the list
maximum=max(lst)
print("Maximum value=",maximum)

#finding minimum value from the list
minimum=min(lst)
print("Minimum value=",minimum)'''