student={"rollno":109,"name":"rijo","total":55}
print(student)
print(student["name"]) #printing stud name

print("college" in student) #checking the key college

student["college"]="Luminar Technolabs" #adding new key value pair

student["total"]+=45 #update the total marks as 100

print(student)

#iteration through the dictionary

for key in student:
    print(key,":",student[key])