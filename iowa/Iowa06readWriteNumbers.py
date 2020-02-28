#programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
def ifPositive(n):                         #function to find positive numbers
    return n>0
f=open("numbers.txt","r")                  #read file "numbers.txt"
fout = open("output.dat", "w")             #create file "output.dat"
fout.close()
List=[]                                    #the list for storing all numbers
for line in f:
    List=line.split()                      #concatenate all numbers into the list
    for i in range(len(List)):             #there is i items in the list
        k=float(List[i])                   #change the type from string to float
        if ifPositive(k):                  #to determine if the number is positive
            fout = open("output.dat", "a") #add positive number to "output.dat"
            fout.write(List[i]+"\n")
f.close()
