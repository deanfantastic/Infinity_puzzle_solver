#!/usr/bin/env python
# # Python 3.7
#
# Dean Crouch

# import tools
import time
import itertools
import numpy as np
import locale
import math

locale.setlocale(locale.LC_ALL, 'en_US')
## Debug smaller puzzle set
Debug_puzzle = True


# Set up arrangement of 15 tiles
tiles = np.array([
    ['black','black','pink','black'],\
 #   ['blue','blue','blue','blue'],\
 #   ['purple','purple','purple','purple'],\
    ['banana','banana','banana','banana'],\
    ['banana','banana','banana','banana'],\
    ['pink','pink','pink','pink'],\
    ['green','green','green','green'],\
    ['yellow','yellow','yellow','yellow'],\
    ['orange','orange','orange','orange'],\
    ['pink','blue','black','purple'],\
    ['pink','yellow','green','orange'],\
    ['pink','orange','yellow','blue'],\
    ['pink','black','orange','purple'],\
    ['black','blue','purple','orange'],\
    ['yellow','green','purple','blue'],\
    ['yellow','black','orange','green'],\
    ['yellow','orange','pink','purple']
    ])

# Define a function to get a tile and return it turned 90 degrees.
# This will create a 2nd, 3rd and 4th column in tiles of the same tiles in a rotated config.
def tile_rotator(tile, turns):

    if (turns == 0):
        new_tile = [tile[0],tile[1],tile[2],tile[3]]
    elif (turns == 1):
        new_tile = [tile[1],tile[2],tile[3],tile[0]]
    elif (turns == 2):
        new_tile = [tile[2],tile[3],tile[0],tile[1]]
    elif (turns == 3):
        new_tile = [tile[3],tile[0],tile[1],tile[2]]

    return list(new_tile) # return new tile orientation.




# If DEBUG = true then print out the full range of 15 tiles in all 4 rotations
if Debug_puzzle == True and False:
    for i in range(0,15):
        for j in range(0,4):
            print(i, ":", j, " - in:", list(tiles[i]), " out:", list(tile_rotator(tiles[i],j)))





# set up some counters etc
time_log = time.time()
config_counter = 0
max_sequence_length = len(tiles)
display_interval = 10000000

#perm_range = ([1,2,3,4,5,6,7,8,9])
#print("Combos: ", format(math.factorial(len(tiles)),',d'))




# Define functions
def tile_comparitor (tile_sequence):
    # first and second tiles are passed as full lists of 4 elements (colours).
    # only a single comparison made on the appropriately facing edges of the tile,
    # based on the direction.
    #print("Tile sequence:", tile_sequence)
    

    # set compare_result to true by default - a failure ot match will make it false. 
    # Accounts for first tile which is not compared to anything.
    compare_result = True
    last_tile = len(tile_sequence)
    #print("Tile Sequence length:", last_tile)

    curr_tile = tile_rotator(tiles[tile_sequence[last_tile-1][0]],0)

    # compare last tile with tile above (if appropriate, ie not first row 0-2)
    if last_tile >3:
        tile_up = tile_rotator(tiles[tile_sequence[last_tile-4][0]],0)
        compare_result = curr_tile[0] == tile_up[2]

    # compare last tile with tile to left (if appropriate ie not divisible by 3 etc)
    if (last_tile)%3+1 >0:
        tile_left = tile_rotator(tiles[tile_sequence[last_tile-2][0]],0)
        compare_result = curr_tile[3] == tile_left[1]

    # return a true if direction compare matches
    print("Compare result:", compare_result, "-", len(tile_sequence))

 
    # If the sequence is 15 long and last compare is true, the sequence is a true solution.
    # Print it out and then reset compare to false so the incrementation process will
    # continue.
    if compare_result == True and len(tile_sequence) == max_sequence_length:
        print("Solution found:")
        for x, y in enumerate(tile_sequence): 
            print(x, ":", y)
        compare_result == False
        print("Compare result flipped to False")



    # True = add new tile to seq
    # False = rotate/inc last tile or rotate/inc previous tile in sequence

    # Need to capture the last sequence case????

    return compare_result




# initiate the tile sequence function which will internal recursion to call itself and 
# make it's way through the sequence options.
tile_sequence = np.array([[0,0],[2,0],[3,0],[4,0]])

# throw initial sequence in the comparitor
tile_comparitor(tile_sequence)



