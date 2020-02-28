#programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
import random
def fastTwoDRandomWalk2(n = 100, printOn = False, jump = 2):
    location_x = 0
    location_y = 0
    length = 0
    step_x = 0
    step_y = 0

    while (abs(location_x)< n and abs(location_y)< n):
        pace = random.randint(1, jump)     # to determine how many paces we walk in once
        step = random.randint(0, 3)        # we have 4 directions, west, east, south, north
        if step == 0:                      # 0 indicates west 
            step_x = -1 * pace             # hence x direction will be negative and move in random paces
            temp_x = location_x + step_x   # to know the temporary location
            if n >= abs(temp_x):           # to ensure robot won't move outside
                location_x = temp_x        # update x location
            else:
                break
        if step == 1:                      # 1 indicates east
            step_x = 1 * pace              # hence x direction will be positive and move in random paces 
            temp_x = location_x + step_x   # to know the temporary location
            if n >= abs(temp_x):           # to ensure robot won't move outside
                location_x = temp_x        # update x location
            else:
                break
        if step == 2:                      # 2 indicates south
            step_y = -1 * pace             # hence y direction will be negative and move in random paces
            temp_y = location_y + step_y   # to know the temporary location
            if n >= abs(temp_y):           # to ensure robot won't move outside
                location_y = temp_y        # update y location
            else:
                break
        if step == 3:                      # 3 indicates north
            step_y = 1 * pace              # hence y direction will be positive and move in random paces
            temp_y = location_y + step_y   # to know the temporary location
            if n >= abs(temp_y):           # to ensure robot won't move outside
                location_y = temp_y        # update y location
            else:
                break
        if printOn == True:                # print location if printOn is true
            print (location_x, location_y)                           
                                       
        step_x = 0                         # we should set the directions to zero, so that
        step_y = 0                         # direction from previous iteration is nor repeated
        length = length + pace             # update the length
    
    return length

#main program
print (fastTwoDRandomWalk2())