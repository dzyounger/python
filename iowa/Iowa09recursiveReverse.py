#Dai Zhaoyang
#22C:016:A06
#ID: 00719596

def recursiveReverse(L):
    #base
    K=[]
    if len(L)==1 or L==[]:
        K+=L
        return K
    else:
        K.append(L[len(L)-1])
        L.pop()
        return K+recursiveReverse(L)