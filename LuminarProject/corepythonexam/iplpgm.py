f=open("ipl","r")
#no,team,matches,win,loss,pts
ipldict={}

for lines in f:
    ipl=lines.rstrip("\n").split(",")

    no=ipl[0]
    team=ipl[1]
    matches=ipl[2]
    win=ipl[3]
    loss=ipl[4]
    pts=ipl[5]


    if no not in ipldict:
        ipldict[no]={"no":no,"team":team,"matches":matches,"win":win,"loss":loss,"pts":pts}
    else:
        pass
for key,value in ipldict.items():
    print(key,"->",value)


def printDetails(**arg):
    num=arg["no"]
    prope=arg["prop"]
    print(ipldict[num]["team"])
    print(ipldict[num][prope])

