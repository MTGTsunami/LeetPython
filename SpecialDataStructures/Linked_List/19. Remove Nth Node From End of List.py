"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        x = head
        y = head
        count = 0
        while x != None:
            count = count + 1
            x = x.next
        target = count - n
        if target == 0:
            head = head.next
        else:
            while target > 1:
                target = target - 1
                y = y.next
            temp = y.next
            y.next = temp.next
            temp.next = None

        return head