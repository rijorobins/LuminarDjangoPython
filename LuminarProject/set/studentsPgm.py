f=open("students","r")
fout=open("fail","r")

set1=set()
set2=set()

for lines in f:
    newlines=lines.rstrip("\n").split(" ")
   # print(newlines)

    set1=set(newlines)
for value in set1:
    print(value)
    #diff=set1.difference(set2)

#for data in set1:
 #   fout.write(str(data)+"\n")



   # print(set1)