"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

from collections import Counter

class Solution_Case189(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 1:
            if t != s:
                return ""
            else:
                return s

        minLength = float('inf')
        index1, index2 = -1, -1
        for x, i in enumerate(s[:len(s) - 1]):
            dic = Counter(t)
            if i in dic:
                dic[i] -= 1
                if dic[i] <= 0:
                    del dic[i]
            for y, j in enumerate(s[x + 1:]):
                if j in dic:
                    dic[j] -= 1
                    if dic[j] <= 0:
                        del dic[j]

                    if dic == {}:
                        length = y + 2
                        if length < minLength:
                            minlength = length
                            index1 = x
                            index2 = x + y + 1
                            break
                else:
                    if dic == {}:
                        index1 = x
                        index2 = x + y

        if index1 != -1 and index2 != -1:
            return s[index1:index2 + 1]
        else:
            return ""


def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if not t or not s:
        return ""

    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = Counter(t)

    # Number of unique characters in t, which need to be present in the desired window.
    required = len(dict_t)

    # left and right pointer
    l, r = 0, 0

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):

        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1

        # Keep expanding the window once we are done contracting.
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]