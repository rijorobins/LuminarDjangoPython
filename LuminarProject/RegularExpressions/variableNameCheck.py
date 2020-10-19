
#rules
#first charcter should be an alphabet a-k
#2nd charcter should be a digit that is divisible by 3
#3rd charcter should be a any sequence of number/letter

import re
#rule="[a-k][369][a-zA-Z0-9]*"



rule="[a-k][369][a-zA-Z0-9]*"

pattern=input("Enter variable name")

matcher=re.fullmatch(rule,pattern)

if matcher==None:
    print("Invalid")
else:
    print("Valid")
