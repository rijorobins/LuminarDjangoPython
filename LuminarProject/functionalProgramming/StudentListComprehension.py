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

objlist=list() #creating a list for storing object,
                # to display the student names who scored greater than 450

for lines in f:
    data=lines.rstrip("\n").split(",")

    rollno=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])

    obj=Student(rollno,name,course,total) #object creation **executes the constructor method

    objlist.append(obj)
#print names of mca students
print("MCA Students")
mca=[obj.name for obj in objlist if obj.course=="mca"]
print(mca)


#convert all the names of the students into upper case

uppername=[obj.name.upper() for obj in objlist]
print(uppername)

#print highest mark

topscore=max([obj.total for obj in objlist])
print(topscore)

#print total marks of all students

totalmarks=sum([obj.total for obj in objlist])
print("grand Total marks:",totalmarks)




