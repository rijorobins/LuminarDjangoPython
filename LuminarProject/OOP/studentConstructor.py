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

st=Student(1000,"rijo","mca",81,6)
st.printStudent()

