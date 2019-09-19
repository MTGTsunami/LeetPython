"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        else:
            mid = int((n - 1) / 2)
            l1 = self.mergeKLists(lists[:mid + 1])
            l2 = self.mergeKLists(lists[mid + 1:])
            l3 = self.mergeTwoCrossLists(l1, l2)
            return l3

    def mergeTwoCrossLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoCrossLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoCrossLists(l1, l2.next)
                return l2
