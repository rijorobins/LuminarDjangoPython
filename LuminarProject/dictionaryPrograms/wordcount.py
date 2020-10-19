
#printing word count of a string(Each word count)

textdata="hello india is my country i love india i am an indian"

dict={}

words=textdata.split(" ")
#print(words)

for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
  #print(lines)



