f=open("emplo","r")

employee={}

for lines in f:
    emp=lines.rstrip("\n").split(",")

    id=emp[0]
    name=emp[1]
    salary=emp[2]
    exp=emp[3]
    desig=emp[4]

    if id not in employee:
        employee[id]={"id":id,"name":name,"salary":salary,"exp":exp,"desig":desig}
    else:
        pass
for key,value in employee.items():
    print(key,"->",value)


def getDetails(**arg):
    eid=arg["id"]
    prope=arg["prop"]
    print(employee[eid]["name"])
    print(employee[eid][prope])
getDetails()

#print(employee)
#def employeedetails(**data):
#       print(employee["id"=1000])