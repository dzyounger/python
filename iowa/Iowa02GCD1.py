#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
a=int(input("Enter the first nonnegative integer"))
b=int(input("Enter the second nonnegative integer"))
Originala=a#initial value a
Originalb=b#initial value b
#loop to apply subtraction repeatedly until the two numbers are equal
while(a!=b):
    #test out the bigger number
    if a>b:
        a=a-b
    else:
        b=b-a
#output
print ("The GCD of",Originala,"and",Originalb,"is",a)