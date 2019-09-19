"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def reverse(head):
            if not head or not head.next:
                return head
            prev = head
            curr = prev.next
            while curr:
                aft = curr.next
                curr.next = prev
                prev = curr
                curr = aft
            head.next = None
            return prev

        if not head or k == 1:
            return head

        count = 1
        cut, newhead, prevheadOdd = head, head, head
        while cut:
            count += 1
            cut = cut.next
            if cut and count % k == 0:
                temp = cut
                cut = cut.next
                temp.next = None
                newhead = reverse(newhead)
                if count == k:
                    head = newhead

                if (count // k) % 2 == 1:
                    if count > k:
                        prevheadEven.next = newhead
                    prevheadEven = cut
                else:
                    prevheadOdd.next = newhead
                    prevheadOdd = cut
                newhead = cut
                count += 1

        if count < k + 1:
            return head
        if ((count - 1) // k) % 2 == 1:
            prevheadOdd.next = newhead
        else:
            prevheadEven.next = newhead
        return head