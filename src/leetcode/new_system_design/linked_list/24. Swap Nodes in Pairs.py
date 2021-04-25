"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            newhead = head.next
            temp1 = head.next  # The second node which needs to be operated.
            while True:
                temp2 = temp1.next  # The third node which needs to be operated.
                if temp2 == None:  # Eventually two nodes left.
                    head.next = None
                    temp1.next = head
                    break
                else:
                    if temp2.next == None:  # Eventually three nodes left
                        head.next = temp2
                        temp1.next = head
                        break
                    else:                   # haven't reached the End...
                        head.next = temp2.next
                        temp1.next = head
                        head = temp2
                        temp1 = temp2.next
        return newhead