#program to convert all the words of the file: demo into uppercase

f=open("demo","r")

capitals=[]

for lines in f:
    newlines=lines.rstrip("\n")
    words=newlines.split(" ")
    for word in words:
        cap=word.upper()
        capitals.append(cap)

        #This can also be combined as:
        #capitals.append(word.upper())
print(capitals)





















'''f=open("demo","r")
upper=[]
for newlines in f:
    newline=newlines.rstrip("\n")
    words=newline.split(" ")
    for word in words:
        upper.append(word.upper())
print(upper)'''