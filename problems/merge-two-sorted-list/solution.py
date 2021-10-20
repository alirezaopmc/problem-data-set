# creating an empty list
lst1 = []
lst2 = []

# number of elements as input
n1 = int(input())

# iterating till the range
if(n1>0):
    elements = input()
    lst1 = [int(x) for x in elements.split(" ")]
    
n1 = int(input())
if(n1 >0):
    elements = input()
    lst2 = [int(x) for x in elements.split(" ")]
lst3=[]


def mergeArrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
 
    # Traverse both array
    while i < n1 and j < n2:
     
        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
     
 
    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
 
    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
        
    return arr3

arr3 =mergeArrays(lst1,lst2,len(lst1), len(lst2))
for i in arr3 :
    print(i,end=' ')
print('')
