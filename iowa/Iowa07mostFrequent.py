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