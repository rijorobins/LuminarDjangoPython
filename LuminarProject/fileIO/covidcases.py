#finding the state wise confirmed cases


f=open("completecovid","r")
fout=open("covidoutput.txt","w")# reference to write to another file named:covidoutput.txt

dict={}

for lines in f:
    dta=lines.rstrip("\n").split(",")
    print(dta)

    state=dta[1]
    confirmed=dta[4]

    if state not in dict:
        dict[state]=confirmed
    else:
        dict[state]=confirmed
print(dict)

#Finding the state that has most confirmed cases

lst=[]

for key,value in dict.items():
    lst.append((value,key))

lst=sorted(lst,reverse=True) #sorting the list
print(lst)
print(lst[0])

#Writing the output of the above list into another file named:covidoutput.txt

for value in lst:
    fout.write(str(value)+"\n")


