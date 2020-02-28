#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596

# Two words are neighbors if they differ in exactly on letter.
# This function returns True if a given pair of words are neighbors
def areNeighbors(w1, w2):
    count = 0
    # if capitals of two words are the same,test the rest four words
    if w1[0] == w2[0]:
        for i in range(4):
            if w1[1:][i] != w2[1:][i]:
                count = count + 1
    # if the rest four words are the same, two words are neighbors
    if w1[1:] == w2[1:]:
        count = 1        
    
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
    
# Explores the network of words D starting at the source word. If the exploration ends
# without reaching the target word, then there is no path between the source and the target.
# In this case the function returns False. Otherwise, there is a path and the function
# returns True.
def searchWordNetwork(source, target, D):

    # Initialization: processed and reached are two dictionaries that will help in the 
    # exploration. 
    # reached: contains all words that have been reached but not processed.
    # processed: contains all words that have been reached and processed, i.e., their neighbors have also been explored.
    # The values of keys are not useful at this stage of the program and so we use 0 as dummy values.
    processed = {source:0}
    reached = []
    for e in D[source]:
        reached.append(e) # the value in the dictionary of a key k is the "parent" of k
        
    
    # Repeat until reached set becomes empty or target is reached 
    while reached:
        # Check if target is in reached; this would imply there is path from source to target
        if target in reached:
            
            processed.update({target:source})
            return processed
        
        # Pick an item in reached and process it
        item = reached.pop() # returns an arbitrary key-value pair as a tuple
        newWord = item
        parent = source
        
        # Find all neighbors of this item and add new neighbors to reached
        processed[newWord] = parent
        for neighbor in D[newWord]:
            if neighbor not in reached and neighbor not in processed:
                reached.append(neighbor)
                source=newWord

    return []

# Given the collection of processed words and their parents, this function starts from
# the target word and walks backs by going to parent, grandparent, great-grandparent, etc.
# all the way back to the source in order to extract the path that the was discovered betwee
# source and target words
def findPath(tree, source, target):
    path = [target] 
    word = target
    while word != source:
        word = tree[word]
        path.append(word)
  
    path.reverse()
    return path
    
        
# Main program
wordList = []
D = {}
readWords(wordList, D)
buildDictionary(wordList, D)

source = input("Please type the source word: ")
target = input("Please type the target word: ")

tree = searchWordNetwork(source, target, D)
if tree:
    print (tree[target])
    print (findPath(tree, source, target))
else:
    print ("There is no path from", source, "to", target)