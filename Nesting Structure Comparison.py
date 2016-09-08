# -*- coding: utf-8 -*-
"""
Nesting Structure Comparison

Instructions
Output
Complete the method (or function in Python) to return true when its argument is
an array that has the same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""
"""
This is my first attempt. Then I failed the test below.
Testing to see if you tried a certain short-cut
✘  [1,'[',']'] same as ['[',']',1]: False should equal True
So I realize maybe the kata wants me to do something else. 
"""
import re
def same_structure_as(original, other):
    original_string = re.sub(r'[^[\](){}]', ' ', str(original))
    other_sring = re.sub(r'[^[\](){}]', ' ', str(other))
    return original_string == other_sring


"""
then I end up something like this...
After I saw the final answer, I realize that I should have treat set or dict as an element... 
Since they are not arrays...
"""
def same_structure_as(original,other):
    if type(original) is not type(other):
        return False
    if len(original) != len(other):
        return False
    if not original:
        return True
        
    if type(original) is type(other):
        if isinstance(original, tuple):
            original = list(original)
            other = list(other)
        elif isinstance(original, set):
            original = sorted(original, key = type)
            other = sorted(other, key = type)
        elif isinstance(original, dict):
            original = sorted([[k, v]for k, v in original.items()], key = lambda l: type(l[1]))
            other = sorted([[k, v]for k, v in other.items()], key = lambda l: type(l[1]))
    
    if isinstance(original[0], list) ^ isinstance(other[0], list):
        return False
    else:
        if isinstance(original[0], list):
            if (len(original) == 1):
                return same_structure_as(original[0], other[0])
            else:
                return same_structure_as(original[0], other[0]) & same_structure_as(original[1: ], other[1: ])
        else:
            if (len(original) == 1):
                return True
            else:
                return same_structure_as(original[1: ], other[1: ])
            


    
[1, '[', ']'] ['[', ']', 1]
original = [ 1, [ 1, 1 ] ]
other = [ 2, [ 2, 2 ] ]
same_structure_as(original,other)

original = 1
other = [ ]
same_structure_as(original,other)



original = [1, '[', ']']
other = ['[', ']', 1]





















