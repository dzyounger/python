#Dai Zhaoyang
#22C:016:A06
#ID: 00719596
n=int(input("Enter a nonnegative integer"))
suffix=""
originalN=n
while n>0:
    suffix=str(n%3)+suffix
    n=n/3
print ("the ternary equivalent of",originalN,"is",suffix)