#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID:00719596
import time                    #call the time and random function
import random
startTime = time.time()        #get the time as the program starts
n=50
L={}
a=0
while len(L.keys())<500000:    #to test the keys rather than test the value
    a=random.randint(1,1000000)
    if a not in L.keys():      #to test if the random number in L
        L[a]=0
    else:
        L[a]+=1

endTime = time.time()          #get the time as the program ends
print (endTime - startTime)      #compute the time of we execute this program