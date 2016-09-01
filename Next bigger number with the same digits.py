"""
Next bigger number with the same digits

Instructions
Output
You have to create a function that takes a positive integer number and returns 
the next bigger number formed by the same digits:

next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
"""


def next_bigger(n):
    digits = list(reversed(str(n)))
    digits_leftest = {}
    previous_max = '0'
    for pos, digit in enumerate(digits):
        if digit < previous_max:
            rightest_bigger_digit_pos = min(p for d, p in digits_leftest.items() if d > digit)
            digits[pos], digits[rightest_bigger_digit_pos] = digits[rightest_bigger_digit_pos], digits[pos]
            """
            After the switch, the number is bigger than original regardless of order of digits to the right
            Then sort the right digits in descending order (right to left) will make right part samllest.
            """
            return int( ''.join(reversed(sorted(digits[:pos], key = lambda d: - int(d)) + digits[pos:])))
        else:
            previous_max = digit
        digits_leftest[digit] = pos
    return -1

next_bigger(12)
next_bigger(513)
next_bigger(2017)
next_bigger(155)
next_bigger(890) 


