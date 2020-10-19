#method overriding

class Parent:
    def phone(self):
        print("Nokia")

class Child(Parent):
    def phone(self):
        print("samsung phone")

ch=Child()
ch.phone()