#Employee details
#print all employees who have salary greater than 20000
#print the name of the employee who have high salary

from functools import *

class Employee:
    def __init__(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
    def printEmployee(self):
        print("id:",self.id)
        print("Name:",self.name)
        print("Designation:",self.designation)
        print("Salary:",self.salary)
    def __str__(self):
        return str(self.name)


f=open("EmployeeData","r")

objlist=[]
salarylist=[]

for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)

    id=data[0]
    name=data[1]
    designation=data[2]
    salary=int(data[3])

    obj=Employee(id,name,designation,salary) #object creation,invokes constructor
    print("obje",obj)
    objlist.append(obj)

# find all employees whose designation=Developer
print("list of developers")
devop = list(filter(lambda obj: obj.designation == 'developer', objlist))
for i in devop:
    print(i)



#convert all employee names to upper case

names=list(map(lambda obj:obj.name.upper(),objlist))
print(names)

#find total salary of all employees

totalsal=reduce(lambda salary1,salary2:salary1+salary2,list(map(lambda obj:obj.salary,objlist)))
print("Total salary of all employees:",totalsal)


#find highest salaried employee

highsalary=reduce(lambda salary1,salary2:salary1 if salary1>salary2 else salary2,list(map(lambda obj:obj.salary,objlist)))

print("Highest salary:",highsalary)
