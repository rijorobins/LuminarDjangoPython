import re

f=open("variableListFile","r")
fout=open("VariableNAmeOutput","w")
varlist=[]
for var in f:
    variables=var.rstrip("\n")
    varlist.append(variables)

rule="[a-l][369][a-zA-Z0-9]*"

for items in varlist:
    matcher=re.fullmatch(rule,items)
    if matcher==None:
        print("Invalid")
    else:
        print("Valid")
        fout.write(items+"\n")