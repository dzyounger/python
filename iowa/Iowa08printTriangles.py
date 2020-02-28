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
G=[]
readWords(wordList, D)
buildDictionary(wordList, D)
# Open a file "triangle" to write outputs
fout=open("homework8triangle.txt","w")
K=D.items()
# To test if all two-word pairs in the list of the values in dictionary "D" are neighbors
for i in range(len(K)):
    for j in range(len(K[i][1])):
        for l in range(len(K[i][1])):
            if areNeighbors(K[i][1][j],K[i][1][l]):
                L=[K[i][0],K[i][1][j],K[i][1][l]]
                L.sort()
                if L not in G:
                    G.append(L)
for i in range(len(G)):
    # Write outputs
    fout.write(G[i][0]+" "+G[i][1]+" "+G[i][2]+"\n")
fout.close()
        
        