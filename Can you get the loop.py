# -*- coding: utf-8 -*-
"""
Can you get the loop ?

Instructions
Output
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.

Image and video hosting by TinyPic
# Use the `next' attribute to get the following node

node.next
"""


class Node:
    '''
    This class is basically trying to replicate the behavior in the question.
    I added the repr for node for easier debug.
    '''
    def __init__(self, node = None, rep = 1):
        self.node = node
        self.rep = rep
        
    def __repr__(self):
        return str(self.rep)
        
    def get_next(node):
        return node.node
        
    def set_next(node, next_node):
        node.node = next_node
        if next_node.rep == 1:
            next_node.rep = node.rep + 1
    
    next = property(fget = get_next, fset = set_next)


def loop_size(node):
    visited = set([])
    while node not in visited:
        visited.add(node)
        node = node.next
    del visited
    
    loops = set([])
    while node not in loops:
        loops.add(node)
        node = node.next
    return len(loops)
        


node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

node4.next == node2

loop_size(node1)

"""
This is the "best practice" solution from laoris.
The complexity is in the chasing phase is something about l - t%l. This wouldn't stuck too long as I thougt.
"""
def loop_size(node):
    turtle, rabbit = node.next, node.next.next
    
    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count
