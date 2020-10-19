#Eg of multiple inheritance

class Parent:
    def method1(self):
        print("Inside parent class")

class Child(Parent):
    def method2(self):
        print("Inside child class")
class Subchild(Child):
    def method3(self):
        print("Inside subchild")
 #object of subchild
#can call three methods
sub=Subchild()

sub.method3()
sub.method2()
sub.method1()

#object of child class can ony call method1() & method2()

chi=Child()
chi.method2()
chi.method1()

#object of Parent class can only call method1()

par=Parent()
par.method1()
