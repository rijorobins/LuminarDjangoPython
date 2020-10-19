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
    objlist.append(obj)


#find all the employees whose designation="developer"

devop=[emp.name for emp in objlist if emp.designation=='developer']
print("list of developers")
for devo in devop:
    print(devo)

#convert the names of employee into upper case

uppername=[obj.name.upper() for obj in objlist]
print(uppername)

#find total salary of all employees

totsal=sum([obj.salary for obj in objlist])
print("Total salary",totsal)

#Find employee who has maximum salary

highperk=max([obj.salary for obj in objlist])
print("Highest salary",highperk)