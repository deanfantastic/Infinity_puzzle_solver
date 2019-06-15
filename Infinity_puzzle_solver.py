#!/usr/bin/env python
# # Python 3.7
#
# Dean Crouch

# Set up pieces the SAME pieces, that is, rotation is ineffective
pieces = []
pieces.append(['black','black','black','black','same'])
pieces.append(['blue','blue','blue','blue','same'])
pieces.append(['purple','purple','purple','purple','same'])
pieces.append(['pink','pink','pink','pink','same'])
pieces.append(['green','green','green','green','same'])
pieces.append(['yellow','yellow','yellow','yellow','same'])
pieces.append(['orange','orange','orange','orange','same'])
# Set up mixed pieces
pieces.append(['pink','blue','black','purple','mixed'])
pieces.append(['pink','yellow','green','orange','mixed'])
pieces.append(['pink','orange','yellow','blue','mixed'])
pieces.append(['pink','black','orange','purple','mixed'])
pieces.append(['black','blue','purple','orange','mixed'])
pieces.append(['yellow','green','purple','blue','mixed'])
pieces.append(['yellow','black','orange','green','mixed'])
pieces.append(['yellow','orange','pink','purple','mixed'])

for i in range(len(pieces)):
    print(str(i) + ': ' + str(pieces[i]))

# Set up arrangement

# Design comparitor 

# Run combos