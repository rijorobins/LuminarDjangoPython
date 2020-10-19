inp="HHPPPSDAAA"

dict={}

letter=1
for letter in inp:
    if letter not in dict:
        dict[letter]=1
    else:
        dict[letter]+=1
print(dict)

output=""#empty string
for k,v in dict.items():
    output=output+str(v)+k
print(output)