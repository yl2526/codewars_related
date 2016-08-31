# -*- coding: utf-8 -*-
"""
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:

Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u.

Example:

dbl_linear(10) should return 22

Note:

Focus attention on efficiency
"""

def dbl_linear(n):
    numbers = {1}
    new_numbers = {1}
    while (len(numbers) - 1) < n:
        new_numbers = {2*num+1 for num in new_numbers}.union({3*num+1 for num in new_numbers})
        numbers = numbers.union(new_numbers)
    numbers = sorted(numbers)
    return numbers[n]
"""
Above is what I tried to do the first. Then I got error dbl_linear(50) = 189.
Because 79 is still in the latest new_numbers, 159 = 79*2+1 has not been added numbers list. 
As n gets larger, this will just become more and more serious.

Below is the result for new_numbers before and after each iteration.
[1]
[3, 4]

[3, 4]
[7, 9, 10, 13]

[7, 9, 10, 13]
[15, 19, 21, 22, 27, 28, 31, 40]

[15, 19, 21, 22, 27, 28, 31, 40]
[39, 43, 45, 46, 55, 57, 58, 63, 64, 67, 81, 82, 85, 94, 121]

[39, 43, 45, 46, 55, 57, 58, 63, 64, 67, 81, 82, 85, 94, 121]
[79, 87, 91, 93, 111, 115, 117, 118, 127, 129, 130, 135, 136, 139, 163, 165, 166, 171, 172, 175, 189, 190, 193, 202, 243, 244, 247, 256, 283, 364]


Thus, I should have used a sorted set or tree to track the nth item.
But such thing doesn't exist in the standard libs.
"""

# this is correct but will time out, perhaps because of the repeatitive min on the whole set
def dbl_linear(n):
    numbers = {1}
    for i in range(n):
        head = min(numbers)
        numbers.add(head*2+1)
        numbers.add(head*3+1)
    return min(numbers)

# finally, I end up something like this. kind of frustrated
from collections import deque
def dbl_linear(n):
    head = 1
    numbers2 = deque([])
    numbers3 = deque([])
    for i in range(n):
        numbers2.append(head*2+1)
        numbers3.append(head*3+1)
        head = min(numbers2[0], numbers3[0])
        if head == numbers2[0]:
            numbers2.remove(head)
        if head == numbers3[0]:
            numbers3.remove(head)
    return head

dbl_linear(50)

correct = [
    1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, 28, 31, 39, 40, 43, 45, 46, 55, 
    57, 58, 63, 64, 67, 79, 81, 82, 85, 87, 91, 93, 94, 111, 115, 117, 118, 121, 
    127, 129, 130, 135, 136, 139, 159, 163, 165, 166, 171, 172, 175, 183, 187, 
    189, 190, 193, 202, 223, 231, 235
    ]
