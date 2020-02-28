#Zhaoyang Dai
#22C:016:A06
#ID:00719596
import math
M=int(input("Enter a positive integer"))
a=1#initial value of a
b=a+1#to ensure b is bigger than a
c=b+1#to ensure c is bigger than b
count=0#to count the number of pythagorean quadruples
#loop to generate all possible pythagorean quadruples
while (a<=b<=c<=M):
    d=math.sqrt(a**2+b**2+c**2)
    #loop to generate the possible pythagorean quadruples when a is unchanged
    while (b<=c<=M):
        #loop to generate the possible pythagorean quadruples when b is unchanged
        while (c<=M):
            #test if d is an integer
            if (d*10%10==0):
                d=int(d)
                count=count+1
                #output
                print (count,a,b,c,d)
            c=c+1
            d=math.sqrt(a**2+b**2+c**2)            
        b=b+1
        c=b+1
        d=math.sqrt(a**2+b**2+c**2) 
    a=a+1
    b=a+1
    c=b+1 
#output
print ("Done")