#Emplyee details


dict={"id":100,"name":"Blesson","designation":"accountant"}



#Add another field salary

dict["salary"]=67000

#Update salary as 100000

dict["salary"]+=33000

#Checking for a specific key

print("companyname" in dict)

print("id" in dict)

print("id" not in dict)

print("companyname" not in dict)

#Printing all the keys and values from the dict

for key in dict:
    print(key,":",dict[key])

#Printing can also be done as follows
for key,value in dict.items():
    print(key,value)
#print(dict)