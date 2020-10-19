#example of single inheritance
# Child is a sub class
#when the sub class is created it  need to pass the super class name to inherit the properties of super class

class Parent:#Super class
    def phone(self):
        print("i have nokia 5310")

class Child(Parent): #sub class
    pass

ch=Child() #object of sub class
ch.phone()