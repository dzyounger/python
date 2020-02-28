#programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
import random
def manyFastRandomWalks(n = 100, jump  = 1, numReptition = 1):
    count = 0
    total = 0
    
    while (count <= numReptition):
        total = total + fastTwoDRandomWalk1(n, False, jump)
        #to repeat add up the length in "numRepetition" times
        count = count +1
        #to count the number of repetition
    return total/numReptition
def fastTwoDRandomWalk1(n = 100, printOn = False, jump = 1):
    location_x = 0
    location_y = 0
    length = 0
    step_x = 0
    step_y = 0

    while (abs(location_x)< n and abs(location_y)< n):
        pace = random.randint(1, jump) 
        # to determine how many paces we walk in once
        step = random.randint(0, 3)    
        # we have 4 directions, west, east, south, north
        if step == 0:           
        # 0 indicates west 
            step_x = -1 * pace  
            # hence x direction will be negative and move in random paces
        if step == 1:           
        # 1 indicates east
            step_x = 1 * pace   
            # hence x direction will be positive and move in random paces
        if step == 2:           
        # 2 indicates south
            step_y = -1 * pace  
            # hence y direction will be negative and move in random paces
        if step == 3:           
        # 3 indicates north
            step_y = 1 * pace   
            # hence y direction will be positive and move in random paces
        location_x = location_x + step_x    # update x location
        location_y = location_y + step_y    # update y location
        if printOn == True:                 
        # print location if printOn is true
            print (location_x, location_y)
        step_x = 0          # we should set the directions to zero, so that
        step_y = 0          # direction from previous iteration is nor repeated
        length = length + pace      # update the length
    
    return length

#main program
print (manyFastRandomWalks())