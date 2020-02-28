import random
import time
def merge(L, first, mid, last):
    
    i = first # index into the first half
    j = mid + 1 # index into the second half

    tempList = []
    
    # This loops goes on as long as BOTH i and j stay within their
    # respective sorted blocks
    while (i <= mid) and (j <= last):
        if L[i] <= L[j]:
            tempList.append(L[i])
            i += 1
        else:
            tempList.append(L[j])
            j += 1
            
    # If i goes beyond the first block, there may be some elements
    # in the second block that need to be copied into tempList.
    # Similarly, if j goes beyond the second block, there may be some
    # elements in the first block that need to be copied into tempList
    if i == mid + 1:
        tempList.extend(L[j:last+1])
    elif j == last+1:
        tempList.extend(L[i:mid+1])
        
    L[first:last+1] = tempList
    

# The merge sort function; sorts the sublist L[first:last+1]    
def generalMergeSort(L, first, last):
    # Base case: if first == last then it is already sorted
    
    # Recursive case: L[first:last+1] has size 2 or more
    if first < last:
        # divide step
        mid = (first + last)/2
        
        # conquer step
        generalMergeSort(L, first, mid)
        generalMergeSort(L, mid+1, last)
        
        # combine step
        merge(L, first, mid, last)
        
        
# Wrapper function
def mergeSort(L):
    generalMergeSort(L, 0, len(L)-1)
    return L
def generateList(n):
    L=[]
    for i in range(n):
        a=random.randint(1,n)
        L.append(a)
    random.shuffle(L)
    return L
def countTime(L):
    start=time.time() 
    B=mergeSort(L)
    end=time.time()
    elapsedTime=end-start
    return B,elapsedTime

# main program
n=int(input("Enter a number,n"))
m=int(input("Enter a number,m"))
tolTime=0
averageTime=0
for a in range(m):
    L=generateList(n)
    tolTime=tolTime+countTime(L)[1]
averageTime=tolTime/m
print (averageTime)
print (countTime(L)[1])