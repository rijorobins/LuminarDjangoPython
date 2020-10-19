#rijorobins@gmail.com

import re

f=open("mailIDFile","r")
fout=open("mailidoutput","w")

idlist=[]
for items in f:
    id=items.rstrip("\n")

    idlist.append(id)

print(idlist)
idrule="[a-z]*\d*[@][a-z]*[.]{1}com"

for ids in idlist:
    matcher=re.fullmatch(idrule,ids)

    if matcher==None:
        print("Invalid")

    else:
        print("Valid")
        fout.write(ids+"\n")
