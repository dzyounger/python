#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID:00719596
def mostFrequent(dictionary):
    k=dictionary.values()                      #get the values of the dictionary
    k.sort()                                   #sort the list k from low to high
    k.reverse()                                #change it from high to low
    L=[]
    m=[]
    for values in k:                           #get the values from the list k
        for i in range(len(k)):                
            if values==dictionary.values()[i]: #to get the corresponding key of the value
                if dictionary.keys()[i] not in L: 
                    L.append(dictionary.keys()[i])
    if len(L)>=50:                             #to get the top 50 words we frequently use
        for i in range(50):
            m.append(L[i])
    else:                                      #see if the dictionary has less than 50 items
        m=L                                    #output all in high to low order
    return m


# Takes a line s and replaces all punctuation marks given
# in the list punctuationMarks by blanks; returns the modified list
def filterOutPunctuation(punctuationMarks, s):
    for mark in punctuationMarks:
        s = s.replace(mark, " ")

    return s

# Turns the lower method into a function
def toLower(s):
    return s.lower()

# Turns all the words in a list to lower case
def makeListLower(wordList):
    return map(toLower, wordList)

# Open the file "War and Peace"
fin = open("homework7war.txt", "r")

wordList = []

# List of all non-letter characters, We will replace these characters in each line by blanks
punctuationMarks = map(chr, range(0, ord("A")) + range(ord("Z")+1, ord("a")) + range(ord("z")+1, 127)) 

# Loop that processes each line of the file
for line in fin:
    newLine = filterOutPunctuation(punctuationMarks, line)
    wordList = wordList + makeListLower(newLine.split())

#Close the input file
fin.close()

dic={}
List=[]
wordList.sort()
previousWord = "" # keeps track of the word most recently output
for word in wordList:
    # only print out new words
    if word != previousWord:
        List.append(word)
        previousWord = word
for i in range(len(List)):
    a=wordList.count(List[i])#get the number of the words
    dic[List[i]]=a
print (mostFrequent(dic))      #get the output
