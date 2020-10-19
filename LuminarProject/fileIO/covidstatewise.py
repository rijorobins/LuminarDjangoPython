f=open("completecovid","r")

covidcases={}

for lines in f:
    cases=lines.rstrip("\n").split(",")
    #print(cases)

    date=cases[0]
    state=cases[1]
    latitude=cases[2]
    longitude=cases[3]
    confirmed=cases[4]
    death=cases[5]
    cured=cases[6]
    newcases=cases[7]
    newdeath=cases[8]
    newrecover=cases[9]

    if state not in covidcases:
        covidcases[state]={"state":state,"latitude=":latitude,"longitude":longitude,"confirmed":confirmed,"death":death,"cured":cured,"newcases":newcases,"newdeath":newdeath,"newrecover":newrecover}
    else:
        pass
for key,value in covidcases.items():
    print(key,"->",value)

