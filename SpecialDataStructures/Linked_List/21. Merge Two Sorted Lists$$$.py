# Amazon OA (new grad)
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Recursive_Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Iterative_Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if not l2 else l2

        return prehead.next



class MySolution_veryOldVersion:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        x = head
        if l1 == None:
            head = l2
        elif l2 == None:
            head = l1
        else:
            while l1 != None and l2 != None:
                if l1.val < l2.val:
                    x.val = l1.val
                    l1 = l1.next
                else:
                    x.val = l2.val
                    l2 = l2.next
                y = x
                x.next = ListNode(None)
                x = x.next
            if l1 == None:
                y.next = l2
            elif l2 == None:
                y.next = l1

        return head
