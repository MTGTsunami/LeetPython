"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return head

        count = 1
        p = head  # p is used to find the position of m
        temp = p
        while count < m:
            temp = p
            p = p.next
            count += 1

        bef = p
        rn = bef.next
        count = 0
        length = n - m
        while count < length:
            aft = rn.next
            rn.next = bef
            bef = rn
            rn = aft
            count += 1

        temp.next = bef
        p.next = rn

        if m != 1:
            return head
        else:
            return bef


