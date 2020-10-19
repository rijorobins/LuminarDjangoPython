import re
#QUANTIFIERS
pattern="aaaaabbbbaabaaabahbaa"
#x="a+" #it will check single and sequence a
#x="a*"
#x="a?"
#x="^a" #checks if given string starting with a or not ?
#x="a$" # checks if given string ends with a or not?
#x="a{2}" #it will check for 2 number of a's
#x="a{2,3}" #minimum 2 a and maximum 3 a


x="a{2,3}"

matcher=re.finditer(x,pattern)
for match in matcher:
    print("LOC",match.start())
    print(match.group())


