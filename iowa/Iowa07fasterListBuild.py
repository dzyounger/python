#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID:00719596
import time               #call the time function
startTime = time.time()   #get the time as the program starts
n = 500000                
L = []
for i in range(n):        
    L.append(i)           #simply get the list L which contains numbers 1-500000
L.reverse                 #because when we insert things to a list, we add this thing to the first position of this list. when we append things, we add this thing to the last position of this list. So, we need to reverse the list.
endTime = time.time()     #get the time as the program ends
print (endTime - startTime) #compute the time of we execute this program