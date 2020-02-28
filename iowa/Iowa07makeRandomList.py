#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID:00719596
import random                        #call the random and time function
import time
startTime = time.time()              #get the time as the program starts
L=[]
i=random.randint(1,1000000)          #get random number in range (1,1000000)
while len(L)!=500000:                #we want the 500000random numbers
    if i not in L:                   #avoid repeat numbers
        L.append(i)                  
        i=random.randint(1,1000000)  
    else:
        i=random.randint(1,1000000)
endTime = time.time()                #get the time as the program ends
print (endTime - startTime)            #compute the time of we execute this program