'''
#convert each record into student object
#1) Print the names of students who scored above 450
#2) Print the student record who has the highest score
#from stud file

class Student:
    def __init__(self,rol,name,course,tot):
        self.rol=rol
        self.name=name
        self.course=course
        self.tot=tot
    def printStud(self):
        print(self.rol)
        print(self.name)
        print(self.course)
        print(self.tot)
    def __str__(self):
        return self.name

f=open("stud","r")

lst=[]

for lines in f:
    data=lines.rstrip().split(",")
    print(data)

    id=data[0]
    name=data[1]
    course=data[2]
    tot=int(data[3])

    obj=Student(id,name,course,tot)

    lst.append(obj)

total=[]

for obj in lst:
    total.append(obj.tot)
maxim=max(total)
for obj in lst:
    if obj.tot>450:
        print("those who scored Greater than 450->",obj) #Print the names of students who scored above 450
    if obj.tot==maxim:
        print("Highes->",obj) #Print the student record who has the highest score'''


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

listtotal=list()#list to store total marks of each object

print("students who scored more than 450:->")

for obj in objlist: #traversing elements in the list

    if obj.total>450:
        print(obj)
    listtotal.append(obj.total)
    maximum=max(listtotal)


print("Topper:->")
for obj in objlist:
    if obj.total==maximum:
        print(obj)






























