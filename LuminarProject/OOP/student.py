class Student:
    def setValues(self,rol,na,cours,tot):
        self.rollno=rol
        self.name=na
        self.course=cours
        self.total=tot
    def printValues(self):
        print("Rollno:",self.rollno)
        print("Name:",self.name)
        print("Course:",self.course)
        print("total:",self.total)
obj=Student()
obj.setValues(12,"Chris","MCA","93")
obj.printValues()