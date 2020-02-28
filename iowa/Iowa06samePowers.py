#programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
def samePowers(n):                   #return a list of m**m in range n
    return map(onePower,range(n))
def onePower(m):                     #function to calculate m**m
    return m**m
#main program
n=int(input("Please give out a positive integer parameter n")) #input n
print (samePowers(n))                  #output the result