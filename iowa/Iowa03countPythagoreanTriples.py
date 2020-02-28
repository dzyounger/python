#Zhaoyang Dai
#22C:016:A06
#ID:00719596
import math
M=int(input("Enter a positive integer"))
x=3#initial value of x
y=x+1#to ensure y is bigger than x
count=0#to count the number of pythagorean triples
#loop to generate all possible pythagorean triples
while (x<=y<=M):
    z=math.sqrt(x**2+y**2)
    #loop to generate the possible pythagorean triples when x is unchanged
    while (y<=M):
        #test if z is an integer
        if (z*10%10==0):
            z=int(z)
            count=count+1
            #output
            print (count,x,y,z)
        y=y+1
        z=math.sqrt(x**2+y**2)
    x=x+1
    y=x+1
#output
print ("Done,","there are",count,"Pythagorean triples")