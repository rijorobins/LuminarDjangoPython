#kl03ad3844

import re

#validate all gmail ids


number_rule="kl\d{2}[a-z]{1,2}\d{4}"
vehicle_number=input("Enter your vehicle number:")
matcher=re.fullmatch(number_rule,vehicle_number)

if matcher==None:
    print("invalid")
else:
    print("valid")

