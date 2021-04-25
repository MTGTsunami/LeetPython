"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        root1, root2 = l1, l2
        while l1 and l2:
            value, rem = divmod(l1.val + l2.val + add, 10)
            l1.val = l2.val = rem
            add = value
            prev1, prev2 = l1, l2
            l1 = l1.next
            l2 = l2.next

        if not l1:
            while l2:
                value, rem = divmod(l2.val + add, 10)
                l2.val = rem
                add = value
                prev2 = l2
                l2 = l2.next
            if add == 1:
                prev2.next = ListNode(add)
            return root2

        if not l2:
            while l1:
                value, rem = divmod(l1.val + add, 10)
                l1.val = rem
                add = value
                prev1 = l1
                l1 = l1.next
            if add == 1:
                prev1.next = ListNode(add)
            return root1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    rl3 = ListNode(0)  # Regard rl3 as a temporary pointer, re as the head pointer of the Linked List
    re = rl3
    list1, list2 = [], []
    while l1 != None:
        list1.append(str(l1.val))
        l1 = l1.next
    while l2 != None:
        list2.append(str(l2.val))
        l2 = l2.next

    list1.reverse()
    list2.reverse()
    s1 = "".join(list1)
    s2 = "".join(list2)
    sum = int(s1) + int(s2)
    s3 = str(sum)
    rlist = list(s3)
    rlist.reverse()

    for i, x in enumerate(rlist):
        rl3.val = int(x)
        if i < len(rlist) - 1:
            rl3.next = ListNode(i + 1)
            rl3 = rl3.next
        else:
            rl3.next = None

    return re  # Accepted





