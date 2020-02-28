#Dai Zhaoyang
#22C:016:A06
#ID: 00719596

import math

class fraction():
    def __init__(self,a,b):
        self.up=a
        self.down=b
    def add(self,b):                #add up
        A1=self.up
        B1=self.down
        A2=b.up
        B2=b.down
        Down=B1*B2
        Up=A1*B2+A2*B1 
        return fraction(Up,Down)
    def subtract(self,b):           #subtract
        A1=self.up
        B1=self.down
        A2=b.up
        B2=b.down
        Down=B1*B2
        Up=A1*B2-A2*B1 
        return fraction(Up,Down)
    def multiple(self,b):           #multiple
        A1=self.up
        B1=self.down
        A2=b.up
        B2=b.down
        Down=B1*B2
        Up=A1*A2
        return fraction(Up,Down)
    def divide(self,b):             #divide
        A1=self.up
        B1=self.down
        A2=b.up
        B2=b.down
        Down=B1*A2
        Up=A1*B2
        return fraction(Up,Down)        
    def __repr__(self):
        A=abs(self.up)
        b=self.down
        a=self.up
        L=1
        for i in range(1,A+1):
            if a%i==0 and b%i==0:
                L=i
        if b/L==1:
            return str(a/L)
        if a==0:
            return 0
        if a*b>0:
            a=abs(a)
            b=abs(b)
        if a*b<0:
            a=-abs(a)
            b=abs(b)
        return str(a/L)+"/"+str(b/L)
    def numerator(self):
        return str(self.up)
    def denominator(self):
        return str(self.down)

#main program    
a=fraction(-50,100)
b=fraction(-8,-4)
print (a.divide(b).numerator())