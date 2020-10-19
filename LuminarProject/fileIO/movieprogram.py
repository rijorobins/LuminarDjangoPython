#manipulations from the file : movies
#Dictionary and File IO

f=open("movies","r")

dict={}
#arranging the films by
for lines in f:
    movies=lines.rstrip("\n").split(",")
    year=movies[2]

    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(dict)


# program to find year in which most films are released

lst=[]

for key,value in dict.items():
    lst.append((value,key))
sortedlist=sorted(lst,reverse=True)
print(sortedlist[0])
























'''
f=open("movies","r")

dict={}

count=0
for lines in f:
    movies=lines.rstrip("\n").split(",")

    year=movies[2]
    print(year)
    count+=1
    print("count=",count)
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
for k,v in dict.items():
    print(k,",",v)

'''