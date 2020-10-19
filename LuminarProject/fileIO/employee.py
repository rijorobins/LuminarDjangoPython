#storing the names of the employees in a list called name[]
#& salaries in the list called salary[] from the file named emplo


f=open("emplo","r")

ename=[]
esalary=[]

for emp in f:
    newlines=emp.rstrip("\n")
    words=newlines.split(",")
    #print(words)

    name=words[1]
    salary=words[2]

    ename.append(name)
    esalary.append(salary)

print("Emplyee Names:",ename)
print("Salary:",esalary)













'''f=open("emplo","r")
name=[]
salary=[]

for names in f:
    line=names.rstrip("\n")
    word=line.split(",")
    ename=word[1]
    esal=word[2]
    name.append(ename)
    salary.append(esal)
print("name:",name)
print("salary:",salary)
'''