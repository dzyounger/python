#Dai Zhaoyang
#22C:016:A06
#ID: 00719596

def sumDigit(n):
    #base
    if n/10==0:
        sum=n
        return sum
    else:
        sum=n%10
        n=n/10
        return sum+sumDigit(n)