#find the no of occurence of the word rijo in the given string
#pattern matching
import re
string="rijosinirijorojiakkurijomanna"
pattern="rijo"

count=0
matcher=re.finditer(pattern,string)
for match in matcher:
    count+=1
    print("Location:",match.start())
    print(match.group())
print("count:",count)
