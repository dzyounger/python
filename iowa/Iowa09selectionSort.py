import random
import time
def swap(L, i, j):
#'''Swaps the elements in the list L at positions i and j'''
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


def selectionSort(L):
#Sorts a list of elements in ascending order by repeatedly selecting
 #  the minimum element from the rest of the list and bringing it to the front.'''

    n = len(L)

    for i in range(n):
        m = min(L[i:])
        j = i + L[i:].index(m)
        swap(L, i, j)

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
    B=selectionSort(L)
    end=time.time()
    elapsedTime=end-start
    return elapsedTime

# main program
n=int(input("Enter a number,n"))
m=int(input("Enter a number,m"))
tolTime=0
averageTime=0
for a in range(m):
    L=generateList(n)
    print (L)
    tolTime=tolTime+countTime(L)
    print (tolTime)
averageTime=tolTime/m
print (averageTime)
    