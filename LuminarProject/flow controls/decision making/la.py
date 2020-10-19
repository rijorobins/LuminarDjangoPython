n1=int(input("Enter n1"))
n2=int(input("Enter n2"))
n3=int(input("enter n3"))


if ( n1 >= n2 & n1 >= n3 ):
    large=n1
elif ( n2 > n1 & n2 > n3):
    print("hhh")
    large=n2
else:
    large=n3
print("Large:",large)

# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
'''num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)'''