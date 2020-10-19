#Finding number of words from the file name:demo

f=open("demo","r")

count=0
#new=[]
for item in f:
    newlines=item.rstrip("\n")
    words=newlines.split(" ")

    for word in words:
        count+=1
print("number of words in file demo=",count)



    #print(words)

    #new.append(newlines)
#print(new)













'''
f=open("demo","r")

count=0
for lines in f:
    newlines=lines.rstrip("\n")#String Literals
    words=newlines.split(" ")#[String,Literals]
    for word in words:
       count+=1
print(words)
print("Count= ",count)

'''