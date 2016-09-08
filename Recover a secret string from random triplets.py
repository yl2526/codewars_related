# -*- coding: utf-8 -*-
"""
There is a secret string which is unknown to you. Given a collection of 
random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter 
occurs somewhere before the next in the given string. "whi" is a triplet 
for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once 
in the secret string.

You can assume nothing about the triplets given to you other than that 
they are valid triplets and that they contain sufficient information to 
deduce the original string. In particular, this means that the secret string
will never contain letters that do not occur in one of the triplets given to you.
"""

def recoverSecret(triplets):
    """triplets is a list of triplets from the secrent string. Return the string."""
    secret = ""
    while triplets:
        possible_next_letter = set([])
        not_next_letter =  set([])
        for triplet in triplets:
            possible_next_letter.add(triplet[0])
            not_next_letter = not_next_letter.union(triplet[1:])
        next_letter = (possible_next_letter -  not_next_letter).pop()
        
        secret += next_letter
        
        for triplet in triplets:
            if next_letter in triplet:
                triplet.remove(next_letter)
        triplets = [triplet for triplet in triplets if triplet != []]

    return secret
                
secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
recoverSecret(triplets)


"""
Below is the solution form ninehills. Really clever. What I did is much more stupid.
"""
def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)
  
def fix(l, a, b):
   """let l.index(a) < l.index(b)"""
   if l.index(a) > l.index(b):
       l.remove(a)
       l.insert(l.index(b), a)