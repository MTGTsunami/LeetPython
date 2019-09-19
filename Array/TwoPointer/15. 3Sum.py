"""

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


def threeSum1(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    rlist = []
    for x, i in enumerate(nums[:-2]):
        for y, j in enumerate(nums[x + 1:-1]):
            for z, k in enumerate(nums[x + 2 + y:]):
                if i + j + k == 0:
                    if [i, j, k] in rlist or [i, k, j] in rlist or [k, i, j] in rlist or [k, j, i] in rlist or \
                            [j, i, k] in rlist or [j, k, i] in rlist:
                        continue
                    else:
                        rlist.append([i, j, k])

    return rlist  # Time limit exceeded （O（n^3））


print(threeSum1([3, -2, 1, 0]))
print(threeSum1([0, 0, 0]))
print(threeSum1([-1, 0, 1, 2, -1, 4]))



def threeSum2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    from collections import Counter

    rlist = []
    temp = []
    hashtable = {}

    for a, b in enumerate(nums):
        hashtable[b] = a
    for x, i in enumerate(nums[:-1]):
        for y, j in enumerate(nums[x + 1:]):
            k = -(i + j)
            if k in hashtable:
                if hashtable[k] > x + y + 1:  # The index of k in hashtable must be bigger than present y
                    if Counter([i, j, k]) not in temp:
                        temp.append(Counter([i, j, k]))
    for ele in temp:
        rlist.append(list(ele.elements()))

    return rlist  # Time limit exceeded O(n^2)


print(threeSum2([3, -2, 1, 0]))
print(threeSum2([0, 0, 0]))
print(threeSum2([-1, 0, 1, 2, -1, 4]))



def threeSum3(nums):  # From CNDS
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums_hash = {}
    result = []
    for num in nums:
        nums_hash[num] = nums_hash.get(num, 0) + 1
    if 0 in nums_hash and nums_hash[0] >= 3:
        result.append([0, 0, 0])

    nums = sorted(list(nums_hash.keys()))

    for i, num in enumerate(nums):
        for j in nums[i + 1:]:
            if num * 2 + j == 0 and nums_hash[num] >= 2:
                result.append([num, num, j])
            if j * 2 + num ==0 and nums_hash[j] >= 2:
                result.append([j, j, num])

            dif = 0 - num - j
            if dif > j and dif in nums_hash:
                result.append([num, j, dif])

    return result


def threeSum4(nums):  # From CNDS 指针对撞
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    result = []
    nums_len = len(nums)
    if nums_len < 3:
        return result
    nums.sort()
    for i in range(nums_len - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        l = i + 1
        r = nums_len - 1
        dif = -nums[i]
        while l < r:
            if nums[l] + nums[r] == dif:
                result.append([nums[l], nums[r], nums[i]])
                while l < r and nums[l] == nums[l + 1]:  # 对于同一个i，可能有多组合适的结果，所以要继续向下寻找
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < dif:
                l += 1
            else:
                r -= 1

    return result
