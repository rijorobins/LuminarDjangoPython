#Separate even numbers in evenlist and odd numbers in oddlist


lst=[10,21,34,45,67,80]
oddlst=[] #Creating an empty list
evenlst=list() #Creating an empty list

#iterate using for loop
for item in lst:
    if(item % 2 == 0):
        evenlst.append(item)
    else:
        oddlst.append(item)
 #printing both lists
print("Oddlist:",oddlst)
print("evenlist:",evenlst)