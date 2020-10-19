f=open("temp","r")

fout=open("tempoutput.txt","w")
dict={}

for words in f:
    newwords=words.rstrip("\n").split(",")
    #print(newwords)

    state=newwords[0]
    temperature=newwords[1]

    if state not in dict:
        dict[state]=state
    else:
        dict[state]=temperature
#print(dict)

lst=[]

for key,value in dict.items():
    lst.append((key,value))

lst=sorted(lst,reverse=True) #sorting the list
print(lst)

for items in lst:
    fout.write(str(items)+"\n")

























