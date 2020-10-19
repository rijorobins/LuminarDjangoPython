#operator overloading


class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self): #invokes when object b is printing
        return str(self.pages)
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __sub__(self, other):
        return self.pages-other.pages
    def __mul__(self, other):
        return self.pages*other.pages

    def __truediv__(self, other):
        return  self.pages/other.pages

b=Book(100)


b1=Book(200)


print(b)
print(b1)

print(b+b1) #overrides the __add__()method

print(b1-b) #overrides the __sub__()method

print(b*b1) #overrides the __mul__()method

print(b1/b) #overrides the __truediv__()method

b2=Book(300)

print(b+b1+b2)

#__str()is the method of object class
#object class is the parentt class for all the classes by default




