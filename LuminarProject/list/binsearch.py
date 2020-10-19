# Check base case

lst=[3,2,5,10,8,1,9,70]

lst.sort()
print(lst)

x=int(input("enter the elemnt to search"))

high=len(lst)
low=0

if high >= low:

    mid = (high + low) // 2

    # If element is present at the middle itself
    if lst[mid] == x:
         x=mid

        # If element is smaller than mid, then it can only
    # be present in left subarray
    elif lst[mid] > x:
        return arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
    else:
        return binary_search(arr, mid + 1, high, x)

else:
    # Element is not present in the array
    return -1

# Function call
result = binary_search(arr, 0, len(arr) - 1, x) 
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") '''