#linear search ,increased complexity
lst=[1,2,3,4,5,6,7,8]
elem=int(input("Enter element to search: "))
flg=0
for item in lst:
    if elem==item:
        flg=1
        break
    #else:
     #   flg=0
if flg==1:
    print("Present")
else:
    print("Not Present")