"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


class MyDPSolution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break

        starAfter = [True] * (n + 1)
        for j in range(1, m + 1):
            temp = [False] * (n + 1)
            temp[0] = dp[0][j]
            for i in range(1, n + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == '*':
                        if starAfter[i]:
                            dp[i][j] = True

                if (not dp[i - 1][j] and dp[i][j]) or temp[i - 1]:
                    temp[i] = True
            starAfter = temp

        return dp[-1][-1]


class DPSolution:
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)

        # init all matrix except [0][0] element as False
        d = [[False] * (n + 1) for _ in range(m + 1)]
        d[0][0] = True

        # DP compute
        for i in range(1, m + 1):
            # the current character in the pattern is '*'
            if p[i - 1] == '*':
                j = 1
                # d[p_idx - 1][s_idx - 1] is a string-pattern match
                # on the previous step, i.e. one character before.
                # Find the first idx in string with the previous math.
                while not d[i - 1][j - 1] and j < n + 1:
                    j += 1
                # If (string) matches (pattern),
                # when (string) matches (pattern)* as well
                d[i][j - 1] = d[i - 1][j - 1]
                # If (string) matches (pattern),
                # when (string)(whatever_characters) matches (pattern)* as well
                while j < n + 1:
                    d[i][j] = True
                    j += 1
            # the current character in the pattern is '?'
            elif p[i - 1] == '?':
                for j in range(1, n + 1):
                    d[i][j] = d[i - 1][j - 1]
                    # the current character in the pattern is not '*' or '?'
            else:
                for j in range(1, n + 1):
                    # Match is possible if there is a previous match
                    # and current characters are the same
                    d[i][j] = d[i - 1][j - 1] and p[i - 1] == s[j - 1]

        return d[-1][-1]


class BackTrackingSolution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            # If the pattern caracter = string character
            # or pattern character = '?'
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern
            elif star_idx == -1:
                return False
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        # The remaining characters in the pattern should all be '*' characters
        return all(x == '*' for x in p[p_idx:])

