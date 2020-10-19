import re

#pattern="[abc]" #it willl check for a or b or c in the target string

#pattern="[a-z]" #check for lowercase alphabets
#pattern="[0-9]" #check for digits
#pattern="[A-Z]"
#pattern="[a-zA-Z]"
#pattern="[a-zA-Z0-9]" #it willl check for all the alphabets and numbers
#pattern="[^a-zA-Z0-9]" #it willl check for all the charcters including space except aphabets and numbers
#pattern="[^0-9]"
#predefined charcters
#pattern="\s" #it will check for space
#pattern="\d" #check for digit =="[0-9]"
#pattern="\D" #check for all chracters except digit=="[^0-9]"
#pattern="\w" #check all except special characters=="[a-zA-Z0-9]"
#pattern="\W" #except nmbers and alphabets=="[^a-zA-Z0-9]"

pattern="[a-zA-Z]"



matcher=re.finditer(pattern,"ag hbFh5TcI @K")
for match in matcher:
    print("Locations:",match.start()) #print the locations
    print(match.group())

