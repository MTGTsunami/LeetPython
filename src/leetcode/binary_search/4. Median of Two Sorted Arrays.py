"""
here are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findKthSortedArrays(nums1, nums2, k):
            m = len(nums1)
            n = len(nums2)

            # array nums1 should be shorter
            if m > n:
                return findKthSortedArrays(nums2, nums1, k)

            # Boundary condition
            if m == 0:
                return nums2[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])

            if (k - 1) / 2 >= m:
                # nums1[(k - 1) / 2] out of range
                cand1 = nums1[m - 1]
                cand2 = nums2[k - m - 1]
                if cand1 == cand2:
                    return cand1
                elif cand1 > cand2:
                    return findKthSortedArrays(nums1, nums2[k - m:], k - (k - m))
                else:
                    return findKthSortedArrays([], nums2, k - m)
            else:
                cand1 = nums1[(k - 1) / 2]
                cand2 = nums2[(k - 1) / 2]
                if cand1 == cand2:
                    return cand1
                elif cand1 > cand2:
                    if k % 2 == 1:
                        return findKthSortedArrays(nums1[:(k - 1) / 2], nums2[(k - 1) / 2:], k - (k - 1) / 2)
                    else:
                        return findKthSortedArrays(nums1[:(k - 1) / 2 + 1], nums2[(k - 1) / 2 + 1:],
                                                   k - ((k - 1) / 2 + 1))
                else:
                    if k % 2 == 1:
                        return findKthSortedArrays(nums1[(k - 1) / 2:], nums2[:(k - 1) / 2], k - (k - 1) / 2)
                    else:
                        return findKthSortedArrays(nums1[(k - 1) / 2 + 1:], nums2[:(k - 1) / 2 + 1],
                                                   k - ((k - 1) / 2 + 1))

        total = len(nums1) + len(nums2)
        if total % 2 == 0:
            return float(
                findKthSortedArrays(nums1, nums2, total / 2) + findKthSortedArrays(nums1, nums2, total / 2 + 1)) / 2
        else:
            return findKthSortedArrays(nums1, nums2, total / 2 + 1)


