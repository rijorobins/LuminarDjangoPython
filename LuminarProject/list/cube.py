#Do the following calculation::
# input:list=[1,4,3]
#output should be 1**1,4**2,3**3
#output=[2,16,27]

lst=[2,4,3]
count=1
op=list()
for item in lst:
    op.append(item**count)
    count+=1
print(op)