"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution(object):  # O(nlogn) time, O(n) space
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        sortlist = []
        scan = head
        while scan is not None:
            sortlist.append(scan.val)
            scan = scan.next

        sortlist.sort()

        scan = head
        ptr = 0
        while scan is not None:
            scan.val = sortlist[ptr]
            scan = scan.next
            ptr += 1
        return head


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class SolutionMergeSort(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:  # find the middle
            fast = fast.next.next
            slow = slow.next
        secondhalf = slow.next
        slow.next = None  # cut down the second half
        l = self.sortList(head)
        r = self.sortList(secondhalf)
        return self.mergeList(l, r)

    def mergeList(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        head = prev = l
        l = l.next
        while l and r:
            if l.val > r.val:
                prev.next = r
                r = r.next
            else:
                prev.next = l
                l = l.next
            prev = prev.next
        if not l:
            prev.next = r
        else:
            prev.next = l
        return head

