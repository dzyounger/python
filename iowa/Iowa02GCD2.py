#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
a=int(input("Enter the larger number"))
b=int(input("Enter the smaller number"))
Originala=a#initial value a
Originalb=b#initial value b
r=a%b
#loop to calculate the remainder of dividing the dividend by the divisor
while(r>0):
    a=b
    b=r
    r=a%b
#output
print ("The GCD of",Originala,"and",Originalb,"is",b)