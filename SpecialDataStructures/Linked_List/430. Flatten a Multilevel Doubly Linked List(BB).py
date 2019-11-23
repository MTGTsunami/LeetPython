"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class MySolution:  # Recursive
    def flatten(self, head: 'Node') -> 'Node':
        def headAndTail(start):
            curr = start
            temp = None
            while curr:
                if curr.child:
                    temp = curr
                    node, end = headAndTail(curr.child)
                    curr = curr.next

                    temp.next = node
                    temp.child = None
                    node.prev = temp

                    if curr:
                        curr.prev = end
                        end.next = curr

                else:
                    temp = curr
                    curr = curr.next
            return start, temp

        return headAndTail(head)[0]


class Solution:  # Iterative
    def flatten(self, head: 'Node') -> 'Node':
        curr, stack = head, []
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next, curr.child.prev, curr.child = curr.child, curr, None
            if not curr.next and stack:
                temp = stack.pop()
                curr.next = temp
                temp.prev = curr
            curr = curr.next
        return head
