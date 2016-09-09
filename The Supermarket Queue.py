# -*- coding: utf-8 -*-
"""
The Supermarket Queue

Instructions
Output
There is a queue for the self-checkout tills at the supermarket. Your task is to
write a function to calculate the total time required for all the customers to 
check out!

The function has two input variables:

customers: an array (list in python) of positive integers representing the queue.
Each integer represents a customer, and its value is the amount of time they 
require to check out.
n: a positive integer, the number of checkout tills.
The function should return an integer, the total time required.

Assume that the front person in the queue (i.e. the first element in the array/list)
proceeds to a till as soon as it becomes free. So, for example:

queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related
idea of a thread pool, with relation to running multiple processes at the same 
time: https://en.wikipedia.org/wiki/Thread_pool
"""

def queue_time(customers, n):
    tills = {i: 0 for i in range(n)}
    while customers:
        current_customer = customers.pop(0)
        tills[min(tills, key = lambda t: tills[t])] += current_customer
    return max(tills.values())
    
a = {1: 'd', 2: 'a'}