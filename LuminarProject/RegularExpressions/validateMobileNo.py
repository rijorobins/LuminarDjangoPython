
#Validate mob no--->>include 91 code and 10 digits

import re
number_rule="(91)?\d{10}" #include 91 code and 10 digits

mobile_number=input("Enter your mobile number")

matcher=re.fullmatch(number_rule,mobile_number)

if matcher==None:
    print("Invalid mobile number")
else:
    print("Valid")
