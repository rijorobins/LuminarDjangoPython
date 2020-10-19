class Person:
    def setValues(self,ag,nam):
        self.age=ag
        self.name=nam
    def printValues(self):
        print("Age=",self.age)
        print("Name=",self.name)

obj=Person()
obj.setValues(27,"Chris")
obj.printValues()

obj1=Person()
obj1.setValues(29,"Bless")

obj1.printValues()