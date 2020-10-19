import re

f=open("VehicleNosFile","r")
fout=open("vehicleNosOutput","w")
vehnolist=[]
for lines in f:
    vehno=lines.rstrip("\n")
    print(vehno)
    vehnolist.append(vehno)
number_rule="kl\d{2}[a-z]{1,2}\d{4}"
for nos in vehnolist:
    matcher = re.fullmatch(number_rule, nos)

    if matcher==None:
        print("invalid")
    else:
        print("valid")
        fout.write(nos+"\n")