#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
def areCollinear(p1, p2, p3):
    a=float(p1[0])           #Changes the number of x,y coordinate to float,
    b=float(p2[0])           #since there is a case that when an integer divided
    c=float(p3[0])           #by another integer, the output would also be 
    d=float(p1[1])           #approximately equal to an integer,it makes the 
    e=float(p2[1])           #output inaccurate.
    f=float(p3[1])    
    if d==e or d==f or e==f:     #prvent the denominator becomes zero
        if a==b==c or d==e==f:   #these are lines which are perpendicular to x,y axis
            return True
        else:
            return False
    else:
        if (a-b)/(d-e)==(b-c)/(e-f):  #if the slope are the same, 3 points are collinear
            return True
        else:
            return False    