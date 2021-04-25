"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MyStackSolution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        length = 0
        scan = head
        while scan is not None:
            length += 1
            scan = scan.next

        stack = []
        count = 0
        scan = head
        if length % 2 == 0:
            mid = -1
        else:
            mid = length // 2 + 1

        while scan is not None:
            count += 1
            if count == mid:
                scan = scan.next
                continue

            if not stack:
                stack.append(scan.val)
            else:
                if scan.val == stack[-1]:
                    stack.pop()
                else:
                    stack.append(scan.val)
            scan = scan.next

        if not stack:
            return True
        else:
            return False


"""
Solution 1: Reversed first half == Second half?

Phase 1: Reverse the first half while finding the middle.
Phase 2: Compare the reversed first half with the second half.
"""


class ReversingTheFirstHalfSolution(object):
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev


