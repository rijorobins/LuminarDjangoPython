#Examle of multiple inheritance
'''
class Parent1:
    def method1(self):
        print("Inside parent 1")

class Parent2:
    def method2(self):
        print("Inside parent 2")
class Child(Parent1,Parent2):
    def method3(self):
        print("Inside child")

ch=Child()

ch.method3()
ch.method2()
ch.method1()
'''
#the above program with same method names in parent1 and Parent2 classes
#compiler will invoke the method included in the first class that is passesd through child class
#python avoid name ambiguity problem(unlike in java)


class Parent1:
    def method1(self):
        print("Inside parent 1")

class Parent2:
    def method1(self):
        print("Inside parent 2")
class Child(Parent1,Parent2):
    def method3(self):
        print("Inside child")

ch=Child()

ch.method3()
ch.method1()
