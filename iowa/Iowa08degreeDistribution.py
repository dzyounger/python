#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596

# Two words are neighbors if they differ in exactly on letter.
# This function returns True if a given pair of words are neighbors
def areNeighbors(w1, w2):
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count = count + 1
    
    return count == 1

# The function reads from the file "words.dat" and inserts the words that are read
# into a list. The words are also inserted into a dictionary as keys, with each key 
# initialized to have [] as its value.
def readWords(wordList, D):
    fin = open("homework8words.dat", "r")

    # Loop to read words from the and to insert them in a list
    # and in a dictionary
    for word in fin:
        newWord = word.strip("\n")
        wordList.append(newWord)
        D[newWord] = []

    fin.close()
    

# Builds the network of words using a dictionary. Two words are connected by an edge in this
# network if they are neighbors of each other, i.e., if they differ from each
# other in exactly one letter.
def buildDictionary(wordList, D):
    numPairs = 0
    # Nested for loop to generate pairs of words
    for i in range(len(wordList)):
        for j in range(i+1, len(wordList)):
            # Check if the two generated words are neighbors
            # if so append word2 to word1's neighbor list and word1 to word2's neighbor list
            if areNeighbors(wordList[i], wordList[j]):
                D[wordList[i]].append(wordList[j])
                D[wordList[j]].append(wordList[i])
    

    
        
# Main program
wordList = []
D = {}
count=0
Dictionary={}
readWords(wordList, D)
buildDictionary(wordList, D)
L1=D.keys()
L2=D.values()
# To get the dictionary which have the degree as keys, and corresponding words as values
for j in range(len(L1)):
    count=len(L2[j])
    if count not in Dictionary.keys():
        Dictionary.keys().append(count)
        Dictionary[count]=[L1[j]]
    else:
        Dictionary[count].append(L1[j])
print (Dictionary)
# Output the degree distribution
for i in range(len(Dictionary.keys())):
    print ("degree",Dictionary.keys()[i]," ",len(Dictionary[Dictionary.keys()[i]]))
