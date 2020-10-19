text="QWEWRTQWERTSWQAQA"

dict={}
for word in text:
    print(word)
    if word not in dict:
        dict[word]=1

    else:
        print(word,"is the first recursive chararter")
        break
print(dict)
























'''text="ABABCCC" #text is a string variable

dict={}
for i in text:
    if i not in text:
        dict[i]=1
    else:
        print(i,"is the 1st recursive character")
        break
'''