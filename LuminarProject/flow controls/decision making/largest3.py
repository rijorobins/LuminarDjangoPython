num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

if num1 > num2 & num1 > num3:
    #print(num1,"is greatst")
    if num2 > num3:
        print(num2,"is Second Largest")
    else:
        print(num3,"is largest")
elif num2 > num1 & num2 > num3:
    print("hello")
    if num1 > num3:
        print(num1,"is greatest")
    else:
        print(num3,"is greatest")
else:
    #print(num3,"is greatest")
    if num1 > num2:
        print(num1,"is greatest")
    else:
        print(num2,"is greatest")
