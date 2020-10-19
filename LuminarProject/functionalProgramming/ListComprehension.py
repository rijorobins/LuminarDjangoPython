#List comprehension

#Program 1:List out all of the possible pairs from this two lists
lst=[1,2,3,4,5,6]
list1=[1,2,3]
list2=[4,5,6]
newlist=[]

newlist=[(i,j) for i in list1 for j in list2]
print("Pairs:",newlist)

#Program2:Find squares of the elemnts of the following list

lst=[1,2,3,4,5,6]
squares=[i*i for i in lst]
print("Squares",squares)

#Program3:Find cubes of the elemnts of the list:lst[]


cubes=[i**3 for i in lst]
print("Cubes:",cubes)

#Program4:fetch even numbers from the list

evens=[i for i in lst if i % 2 == 0]
print("even numbers: ",evens)

#Program 5:store number+1 if number>5 and store number-1 if number<5

lst=[3,6,4,5,7,8,1,2]
newlist=[i+1 if i>5 else i-1 for i in lst]
print("NEwlist:",newlist)