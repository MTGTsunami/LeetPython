"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # find the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        second = self.reverse(second)
        first = head

        # merge the first half and the second half
        while first and second:
            prev1 = first
            first = first.next
            prev1.next = second
            prev2 = second
            second = second.next
            prev2.next = first
        return head

    def reverse(self, head):
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        while curr:
            aft = curr.next
            curr.next = prev
            prev = curr
            curr = aft
        head.next = None
        return prev
