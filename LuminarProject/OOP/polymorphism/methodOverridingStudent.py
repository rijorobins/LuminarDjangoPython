#Overloading
#Student program

class Student:
    college_name="MCET"
    def __init__(self,rollno,name,course,total,sem):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
        self.sem=sem
    def printStudent(self):
        print("Rollno:",self.rollno)
        print("Name:",self.name)
        print("Course:",self.course)
        print("Total:",self.total)
        print("semester:",self.sem)
    def __str__(self): #overrides the __str__() methd of object clas
        return str(self.rollno)+" "+self.name+" "+self.course+" "+str(self.sem)+" "+str(self.total)

obj=Student(13,"rijo","mca",89,4)

print(obj) #when we try to print the object , the __str__() method of the Object class is overrided

#object class is the parent class for all the classes by default