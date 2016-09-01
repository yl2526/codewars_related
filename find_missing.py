"""
Description:

An Arithmetic Progression is defined as one in which there is a constant difference 
between the consecutive terms of a given series of numbers. You are provided with 
consecutive elements of an Arithmetic Progression. There is however one hitch: 
Exactly one term from the original series is missing from the set of numbers 
which have been given to you. The rest of the given series is the same as the 
original AP. Find the missing term.

You have to write the function findMissing (list) , list will always be atleast 
3 numbers. The missing term will never be the first or last one.

Example :

findMissing([1,3,5,9,11]) # => 7
PS: This is a sample question of the facebook engeneer challange on interviewstreet. 
I found it quite fun to solve on paper using math , derive the algo that way. Have fun!
"""

def find_missing(sequence):
    dif = (sequence[-1] - sequence[0]) / len(sequence)
    for pre, cur in zip(sequence[:-2], sequence[1: -1]):
        if (cur - pre) != dif:
            return cur - dif

len([1, 2, 3, 4, 6, 7, 8, 9])
find_missing([1, 2, 3, 4, 6, 7, 8, 9])


"""
topzhangye's solution. interesting
"""
def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)