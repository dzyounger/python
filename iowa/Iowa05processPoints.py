#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
def collinearityTest(pointList):
    n=len(pointList)
    a=0                   #a indicates the first position in pointList
    b=1                   #b indicates the first position in pointList
    c=2                   #c indicates the first position in pointList
    #loop to generate all possible collinear points
    while a<b<c<=n-1:     
        #loop to generate all possible collinear points when a is unchanged
        while b<c<=n-1:
            #loop to generate all possible collinear points when b is unchanged
            while c<=n-1:
                #test if points are collinear
                if areCollinear(pointList[a],pointList[b],pointList[c]):
                    return[pointList[a],pointList[b],pointList[c]]
                c=c+1     #change c
                
            b=b+1         #change b
            c=b+1         #to ensure c is greater than b
            
        a=a+1             #change a
        b=a+1             #to ensure b is greater than a
        c=b+1             #to ensure c is greater than b
        #if there is no output, return an empty list
        if not areCollinear(pointList[a],pointList[b],pointList[c]):
            return []

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
        
#main program
L=[]                            #L is used to concatenate things we input
n=input("Please input the points:") #input the first two numbers
while n:
    point=n.split()             #exchange what we input to a coordinate    
    L.append(point)             #concatenate these coordinate
    n=input()               #input the next two numbers

#output
if collinearityTest(L)==[]:     #to test if there are 3 coordinates that are collinear
    print ("The list contains no collinear triple.")
else:
    list=collinearityTest(L)    #more convinient to find the element in the list
    print ("The points","(",list[0][0],",",list[0][1],")","(",list[1][0],",",list[1][1],")","and","(",list[2][0],",",list[2][1],")","are collinear.")