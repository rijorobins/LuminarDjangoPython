f=open("demo","r")
lst=[]
for i in f:#String Literals\n
    words=i.rstrip("\n")
    wordby=words.split(" ")
    for word in wordby:
        lst.append(word)
print(lst)