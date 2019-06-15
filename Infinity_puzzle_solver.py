#!/usr/bin/env python
# # Python 3.7
#
# Dean Crouch

# import tools
import itertools as iter
import numpy as np

# Set up the SAME tiles, that is, rotation is ineffective
tiles_same = []
tiles_same.append(['black','black','black','black','same'])
tiles_same.append(['blue','blue','blue','blue','same'])
tiles_same.append(['purple','purple','purple','purple','same'])
tiles_same.append(['pink','pink','pink','pink','same'])
tiles_same.append(['green','green','green','green','same'])
tiles_same.append(['yellow','yellow','yellow','yellow','same'])
tiles_same.append(['orange','orange','orange','orange','same'])

# Set up mixed tiles
tiles_mixed = []
tiles_mixed.append(['pink','blue','black','purple','mixed'])
tiles_mixed.append(['pink','yellow','green','orange','mixed'])
tiles_mixed.append(['pink','orange','yellow','blue','mixed'])
tiles_mixed.append(['pink','black','orange','purple','mixed'])
tiles_mixed.append(['black','blue','purple','orange','mixed'])
tiles_mixed.append(['yellow','green','purple','blue','mixed'])
tiles_mixed.append(['yellow','black','orange','green','mixed'])
tiles_mixed.append(['yellow','orange','pink','purple','mixed'])

for i in range(len(tiles_same)):
    print('Same tiles ' + str(i) + ': ' + str(tiles_same[i]))
print(' ')

for i in range(len(tiles_mixed)):
    print('Mixed tiles ' + str(i) + ': ' + str(tiles_mixed[i]))
print(' ')

# Set up arrangement of 5x3 matrix
# SAME tiles cannot be next to each other. The 7 can only fit into the matrix in locations 2, 4, 6, 8, 10, 12 & 14
matrix1 = []
matrix1.append(['mixed','same','mixed','same','mixed'])
matrix1.append(['same','mixed','same','mixed','same'])
matrix1.append(['mixed','same','mixed','same','mixed'])

np.where(matrix1 == 'mixed')

for i in range(len(matrix1)):
    print('Matrix1 ' + str(i) + ': ' + str(matrix1[i]))
print(' ')

matrix2 = []
matrix2.append(['same','mixed','same','mixed','same'])
matrix2.append(['mixed','same','mixed','same','mixed'])
matrix2.append(['mixed','mixed','same','mixed','same'])

for i in range(len(matrix2)):
    print('Matrix2 ' + str(i) + ': ' + str(matrix2[i]))
print(' ')

# Design comparitor 
# each location in the matrix has specific comparisons to the neighbouring tiles, i.e. the first location only compares right and down.
# if the comparitor cell has U R D or L it will compare Up, Right, Down and Left - in that order
comparitor = []
comparitor.append(['R D','R D L','R D L','R D L','D L'])
comparitor.append(['U R D','U R D L','U R D L','U R D L','U D L'])
comparitor.append(['U R','U R L','U R L','U R L','U L'])

for i in range(len(comparitor)):
    print('Comparitor ' + str(i) + ': ' + str(comparitor[i]))
print(' ')

# Run combos
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

#### testing comparitor function
print(tile_comparitor(tiles_same[0],tiles_mixed[0],'D'))



# set up array for SAME tile orders. 7!
tiles_same_order = list(iter.permutations((1,2,3,4,5,6,7), 7))
print('SAME orders:' + str(len(tiles_same_order)))

# set up array for MIXED tile orders. 8!
tiles_mixed_order = list(iter.permutations((1,2,3,4,5,6,7,8), 8))
print('MIXED orders:' + str(len(tiles_mixed_order)))
