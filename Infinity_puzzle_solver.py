#!/usr/bin/env python
# # Python 3.7
#
# Dean Crouch

# import tools
import time
import itertools as iter
import numpy as np
import locale

locale.setlocale(locale.LC_ALL, 'en_US')
## Debug smaller puzzle set
Debug_puzzle = False


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

# Design comparitor
# each location in the matrix has specific comparisons to the neighbouring tiles, i.e. the first location only compares right and down.
# if the comparitor cell has U R D or L it will compare Up, Right, Down and Left - in that order
comparitor = np.array([['R D','R D L','R D L','R D L','D L'],\
    ['U R D','U R D L','U R D L','U R D L','U D L'],\
    ['U R','U R L','U R L','U R L','U L']])


if(Debug_puzzle==True):
    matrix = np.array([\
    [['same','mixed','same'],\
    ['mixed','same','mixed'],\
    ['same','mixed','same']]\
    ])

    # Set up the SAME tiles, that is, rotation is ineffective

    tiles_same = np.array([['black','black','black','black'],\
    ['black','black','black','black'],\
    ['black','black','black','black'],\
    ['black','black','black','black'],\
    ['black','black','black','black']])

    # Set up mixed tiles
    tiles_mixed = np.array([['black','black','black','black'],\
    ['black','black','black','black'],\
    ['black','black','black','black'],\
    ['black','black','black','black']])

    # Design comparitor
    # each location in the matrix has specific comparisons to the neighbouring tiles, i.e. the first location only compares right and down.
    # if the comparitor cell has U R D or L it will compare Up, Right, Down and Left - in that order
    comparitor = np.array([['R D','R D L','D L'],\
    ['U R D','U R D L','U D L'],\
    ['U R','U R L','U L']])



print('Matrix: \n', matrix)
print(' ')

print('Same tiles \n', tiles_same)
print(' ')

print('Mixed tiles \n', tiles_mixed)
print(' ')

print('Comparitor: \n', comparitor)
print(' ')



# set up array for SAME tile orders 7! & MIXED tile order 8!
tiles_same_order = list(iter.permutations((1,2,3,4,5,6,7), 7))
tiles_mixed_order = list(iter.permutations((1,2,3,4,5,6,7,8), 8))

## set up ordered list with smaller debug puzzle set. OVERRIDE
if(Debug_puzzle==True):
    tiles_same_order = list(iter.permutations((1,2,3,4,5), 5))
    tiles_mixed_order = list(iter.permutations((1,2,3,4), 4))

print('SAME orders: ' + str(len(tiles_same_order)))
print('MIXED orders: ' + str(len(tiles_mixed_order)))

print(' ')

# Define functions

def tile_comparitor (first_tile, second_tile, direction):
    # first and second tiles are passed as full lists.
    # only a single comparison made on the appropriately facing edges of the tile,
    # based on the direction.

    # DEBUG line
    ###print(first_tile,'-', second_tile, ' ', direction)

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
config_counter = 1
display_interval = 100000
working_config= []
config_total = len(matrix)*len(tiles_same_order)*len(tiles_mixed_order)



for z in range(0,len(matrix)):
    for y in range(0,len(tiles_same_order)):
        for x in range(0,len(tiles_mixed_order)):
            if(config_counter%display_interval==0):
                print('Config:', locale.format_string("%d", config_counter, grouping=True), '/', locale.format("%d", config_total, grouping=True), 'perms -', end = ' ')
                print(str(z)+'/'+str(len(matrix)),\
                    str(y)+'/'+str(len(tiles_same_order)),\
                    str(x)+'/'+str(len(tiles_mixed_order)),\
                    '|',\
                    len(working_config),'working solutions', end='')
                #print(locale.format("%f", seconds_remaining, grouping=True), '% |', int(time.time() - time_log), ' seconds -', end=' ')

            if(Debug_puzzle==True):
                print(' ')

            # populate the specific configuration for this matrix, sames_order and mixed_order
            config_populate= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

            if(Debug_puzzle==True):
                config_populate= [[0,0,0],[0,0,0],[0,0,0]]

            tiles_same_counter = 0
            tiles_mixed_counter = 0
            for i in range(0,len(matrix[z])):

                for j in range(0,len(matrix[z][0])):

                    if(matrix[z][i][j]=='same'):
                        config_populate[i][j] = tiles_same[(tiles_same_order[(y)][tiles_same_counter])-1]
                        tiles_same_counter += 1

                    else:
                        config_populate[i][j] = tiles_mixed[(tiles_mixed_order[(x)][tiles_mixed_counter])-1]
                        tiles_mixed_counter += 1

            # finished populating the configuration

            # test the config based on the comparitor requirements.
            # pull the tiles which are mixed and can be rotated
            tiles_rotatable = matrix[z]

            # Index over x and y of config
            # If tile is 'mixed' then perform n tests
            # If any tests are false, rotate 90deg and test again
            # valid tile config if all tests are True

            # reset the config test results.
            config_test_result = []

            for i in range(0,len(matrix[z])): # interate through i dimension of tile config (0-4)
                for j in range(0,len(matrix[z][0])): # interate through j dimension of tile config (0-2)

                    tile_spin_test_result = []

                    if(tiles_rotatable[i][j]=='mixed'): # perform tile tests only on tils marked as mixed

                        for l in range(0,4): # loop over tile rotations

                            tests = str.split(comparitor[i][j]) # grad the valid comparisons for each tile in the config. # split into array of single tests
                            #print(tests, end=' ')

                            tile_test_result = [] # reset the tile_test_result - gives a string of results. All true means it's a valid tile placement and rotation.
                            ###print(config_populate[i][j])

                            for k in range(0,len(tests)): # loop through tile tests
                                ### print(i, j, config_populate)

                                if(tests[k]=='U'):
                                    tile_test_result.append(tile_comparitor(config_populate[i][j],config_populate[i-1][j],'U'))

                                elif(tests[k]=='R'):
                                    tile_test_result.append(tile_comparitor(config_populate[i][j],config_populate[i][j+1],'R'))

                                elif(tests[k]=='D'):
                                    tile_test_result.append(tile_comparitor(config_populate[i][j],config_populate[i+1][j],'D'))

                                elif(tests[k]=='L'):
                                    tile_test_result.append(tile_comparitor(config_populate[i][j],config_populate[i][j-1],'L'))

                            try:
                                if(tile_test_result.index(False) >= 0):
                                    tile_spin_test_result.append(False)
                            except ValueError:
                                tile_spin_test_result.append(True)

                            # search for a False in the tile_test_result. No falses means the tile_rotation meets all tests
                            # need to error handle as index without a result throws a valueError.

                            # rotate the tile
                            config_populate[i][j] = tile_rotator(config_populate[i][j])

                        #print(' ')

                        #print('Tile in all rotations: (', i, '-', j, ')')
                        #print(tile_spin_test_result)
                        #print(' ')

                        # If all tile_spins have at least 1 True, then the config is valid. If at least one tile_spin cannot show a match,
                        # then the entire config is invalid

                        # create list of tiles that have a rotation that meets requirements.
                        try:
                            if(tile_test_result.index(False) >= 0):
                                config_test_result.append(False)
                                break
                        except ValueError:
                            config_test_result.append(True)

                        # print list of True tiles in the config
            #print('All tiles in config:')
            #print(config_test_result)
            #print(' ')

            # If the mixed tests return all true in any rotation, the config has a workable solution.
            # Not preserving the rotation state of the tiles, just it's position.
            try:
                if(config_test_result.index(False) >= 0):
                    #print('Config doesnt work')
                    if(config_counter%display_interval==0):
                        print('...')
            except ValueError:
                print('CONFIG WORKS')
                working_config.append([z,y,x])

            config_counter += 1


for d in range(0,len(working_config)):
    print(working_config[d])
