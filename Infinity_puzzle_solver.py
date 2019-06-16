#!/usr/bin/env python
# # Python 3.7
#
# Dean Crouch

# import tools
import time
import itertools as iter
import numpy as np

# Set up the SAME tiles, that is, rotation is ineffective

tiles_same = np.array([['black','black','black','black'],\
    ['blue','blue','blue','blue'],\
    ['purple','purple','purple','purple'],\
    ['pink','pink','pink','pink'],\
    ['green','green','green','green'],\
    ['yellow','yellow','yellow','yellow'],\
    ['orange','orange','orange','orange']])

# Set up mixed tiles
tiles_mixed = np.array([['pink','blue','black','purple'],\
    ['pink','yellow','green','orange'],\
    ['pink','orange','yellow','blue'],\
    ['pink','black','orange','purple'],\
    ['black','blue','purple','orange'],\
    ['yellow','green','purple','blue'],\
    ['yellow','black','orange','green'],\
    ['yellow','orange','pink','purple']])

print('Same tiles \n', tiles_same)
print(' ')

print('Mixed tiles \n', tiles_mixed)
print(' ')

# Set up arrangement of 5x3 matrix
# SAME tiles cannot be next to each other. The 7 can only fit into three arrangewmnts:
# the matrix locations [2, 4] [6, 8, 10] [12, 14]
# the matrix locations [1, 3, 5] [7, 9] [13 15]
# the matrix locations [3, 5] [7, 9] [11, 13, 15]
matrix = np.array([[['mixed','same','mixed','same','mixed'],\
    ['same','mixed','same','mixed','same'],\
    ['mixed','same','mixed','same','mixed']],\
    [['same','mixed','same','mixed','same'],\
    ['mixed','same','mixed','same','mixed'],\
    ['mixed','mixed','same','mixed','same']],\
    [['mixed','mixed','same','mixed','same'],\
    ['mixed','same','mixed','same','mixed'],\
    ['same','mixed','same','mixed','same']]])

print('Matrix: \n', matrix)
print(' ')


# Design comparitor 
# each location in the matrix has specific comparisons to the neighbouring tiles, i.e. the first location only compares right and down.
# if the comparitor cell has U R D or L it will compare Up, Right, Down and Left - in that order
comparitor = np.array([['R D','R D L','R D L','R D L','D L'],\
    ['U R D','U R D L','U R D L','U R D L','U D L'],\
    ['U R','U R L','U R L','U R L','U L']])

print('Comparitor: \n', comparitor)
print(' ')

# set up array for SAME tile orders. 7!
tiles_same_order = list(iter.permutations((1,2,3,4,5,6,7), 7))
print('SAME orders: ' + str(len(tiles_same_order)))

# set up array for MIXED tile orders. 8!
tiles_mixed_order = list(iter.permutations((1,2,3,4,5,6,7,8), 8))
print('MIXED orders: ' + str(len(tiles_mixed_order)))


# Define functions

def tile_comparitor (first_tile, second_tile, direction):
    # first and second tiles are passed as full lists.
    # only a single comparison made on the appropriately facing edges of the tile,
    # based on the direction.

    if direction == 'U':
        compare_result = first_tile[0] == second_tile[2]
    
    elif direction == 'R':
        compare_result = first_tile[1] == second_tile[3]
    
    elif direction == 'D':
        compare_result = first_tile[2] == second_tile[0]
    
    elif direction == 'L':
        compare_result = first_tile[3] == second_tile[1]
    
    else:
        compare_result = 'tile_comparitor function ERROR'

    # return a true if direction compare matches
    return compare_result

def tile_rotator(tile):
    new_tile = np.append(tile, tile[3]) # add a temp 5th element
    for i in range(0,3): # cycle over the original tile to move the index along
        new_tile[i+1] = tile[i]
    new_tile[0] = new_tile[4] # set first element to the same as the tmep 5th
    new_tile = np.delete(new_tile,[4]) # remove the temp 5th element.


    return new_tile # return new tile orientation.

#### testing comparitor function

# cycle through matrix for sames
time_log = time.time()


#### DEBUG
matrix_num = 0
tiles_same_perm = 0
tiles_mixed_perm = 0
#### DEBUG


# populate the specific configuration for this matrix, sames_order and mixed_order
config_populate= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
tiles_same_counter = 0
tiles_mixed_counter = 0
for i in range(3):

    for j in range(5):

        if(matrix[matrix_num][i][j]=='same'):
            config_populate[i][j] = tiles_same[(tiles_same_order[(tiles_same_perm)][tiles_same_counter])-1]
            tiles_same_counter += 1

        else:
            config_populate[i][j] = tiles_mixed[(tiles_mixed_order[(tiles_mixed_perm)][tiles_mixed_counter])-1]
            tiles_mixed_counter += 1
# finished populating the configuration

# test the config based on the comparitor requirements.
# pull the tiles which are mixed and can be rotated
tiles_rotatable = matrix[matrix_num]

# Index over x and y of config
# If tile is 'mixed' then perform n tests
# If no passes, rotate 90deg and test again

for i in range(0,3):
    for j in range(0,5):
        if(tiles_rotatable[i][j]=='mixed'):
            tests = str.split(comparitor[i][j])
            for l in range(0,4):
                for k in range(0,len(tests)):
                    print(config_populate[i][j], end=' ')
                    if(tests[k]=='U'):
                        print(tests[k], tile_comparitor(config_populate[i][j],config_populate[i-1][j],'U'), '[', i, j, ']')
                    elif(tests[k]=='R'):
                        print(tests[k], tile_comparitor(config_populate[i][j],config_populate[i][j+1],'R'), '[', i, j, ']')
                    elif(tests[k]=='D'):
                        print(tests[k], tile_comparitor(config_populate[i][j],config_populate[i+1][j],'D'), '[', i, j, ']')
                    elif(tests[k]=='L'):    
                        print(tests[k], tile_comparitor(config_populate[i][j],config_populate[i][j-1],'L'), '[', i, j, ']')

                config_populate[i][j] = tile_rotator(config_populate[i][j])
            print(' ')

# finished testing the config

# If the mixed tests return all true in any rotation, the config has a workable solution.
# Not preserving the rotation state of the tiles, just it's position.