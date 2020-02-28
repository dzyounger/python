#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
n=input("Please type your text. Type an extra enter when you are done.")  #input the first sentence                                       
letterList=[]                                       #to get the first letter of every word we input
L=[]                                                #the final list L
alphabet=["abcdefghijklmnopqrstuvwxyz"]             #the alphabet we use for calculate
alphabet_capital=["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]     #the capitalized alphabet
while n:
    letter=n.split()                                #to split sentence we input to every single word
    length=len(letter)                              #to know how many letters we have in the sentence
    for l in range (0,length):                      #l indicates numbers 0 to (length-1)
        startWith=letter[l][0]                      #to get the first letter of word we input
        letterList.append(startWith)                #concatenate these letter to a list
    n=input()                                   #input the second sentence
for i in range(0,26):                               #there are 26 letters in the alphabet
    count1=letterList.count(alphabet[0][i])         #to count the letter from the alphabet list from position 0 to 25         
    count2=letterList.count(alphabet_capital[0][i]) #to count the letter from the alphabet_capital list from position 0 to 25      
    count=count1+count2                             #add up the two counts, since we calculate these two kinds of letter as a whole
    L.append(count)                                 #conctenate all counts to a list
#output
print (L)
