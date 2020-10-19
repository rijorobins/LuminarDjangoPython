class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def printStudent(self):
        print("Rollno:",self.rollno)
        print("Name:",self.name)
        print("Course:",self.course)
        print("Total:",self.total)
    def __str__(self): #strig representation of object   ***
        return self.name   #returns the name of the object

f=open("stud","r") #opening the file in read mode

objlist=list() #creating a list for storing object,to display the student names who scored greater than 450

for lines in f:
    data=lines.rstrip("\n").split(",")

#['1005', 'bijoy', 'bca', '450']

    rollno=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])

    obj=Student(rollno,name,course,total) #object creation **executes the constructor method

    objlist.append(obj) #adding objects to the list
#convert all the names to upper
names=list(map(lambda obj:obj.name.upper(),objlist))
print(names)


#students have >450
print("students who scored greater than 450 :")
totals=list(filter(lambda obj:obj.total>450,objlist))
for tot in totals:
    print(tot)
'''
total=list(filter(lambda obj:obj.total>450,objlist))
for i in total:
    print(i)

'''
print("MCA stu")
mca=list(filter(lambda obj:obj.course=='mca',objlist))
for mc in mca:
    print(mc)


