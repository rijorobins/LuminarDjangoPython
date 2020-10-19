lst=[11,23,13,45,10,89,22]
lst.sort() #step 1 :Sort the list
print(lst)

element=int(input("Enter the element to search : "))
#setting lower to 0th position and upper to the last position
lower=0
upper=len(lst)

#find the middle value
mid=(lower+upper)//2

if element < lst[mid]:
    upper=mid-1
    print("Element found")
elif element > lst[mid]:
    lower=mid+1
    print("Element found")
elif element == lst[mid]:
    print("Element found")
else:
    print("Element not found")


