
#Program number1
#input:"HEY"
#output:"HEEYYY"

string="HEY"
count=1

for lines in string:
    print(lines*count,end="")
    count+=1


#inputlist=[4,1,2,5,6,7]
#outputlist=if number > 5 then store number+1 & if number < 5 then store number-1
inputlist=[4,1,2,5,6,7]
outputlist=list()
for item in inputlist:
    if item > 5:
        outputlist.append(item+1)
    elif item < 5:
        outputlist.append(item-1)
print(outputlist)


