'''class Employee():
    company_name="Wipro"
    def setEmp(self,id,designation,salary):
        self.id=id
        self.designation=designation
        self.salary=salary
    def printEmp(self):
        print("id:",self.id)
        print("designation:",self.designation)
        print("salary",self.salary)
        print(""Company name,Employee.company_name)

emp=Employee()

emp.setEmp(1000,"developer",30000)
emp.printEmp()'''


#the above program using constructor

class Employee():
    company_name="Wipro" #Static variable

    def __init__(self,id,designation,salary): #Constructor method
        self.id=id
        self.designation=designation
        self.salary=salary

    def printEmp(self):
        print("id:",self.id)
        print("designation:",self.designation)
        print("salary:",self.salary)
        print("company name:",Employee.company_name)

emp=Employee(10002,"developer",30000) #object creation constructor is automatically invoked at this step
emp.printEmp()
