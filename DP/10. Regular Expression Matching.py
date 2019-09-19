"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

class SolutionGood(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]



class SolutionBad:  # 422 cases passed
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

        dp[0][0] = 1  # both s and p are empty strings
        for i in range(1, m + 1):
            dp[i][0] = 0  # false when p is an empty string
        for j in range(1, n + 1):
            if j % 2 != 0:
                dp[0][j] = 0
            else:
                if p[:j].count("*") == j / 2:
                    dp[0][j] = 1
                else:
                    dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1].isalpha():
                        dp[i][j] = 0
                    else:
                        if p[j - 1] == ".":
                            dp[i][j] = dp[i - 1][j - 1]
                        else:  # when p[j-1] = "*"
                            if p[j - 2] != s[i - 1]:
                                if p[j - 2] != ".":  # like(s:a, p:a*c*)
                                    dp[i][j] = dp[i][j - 2]
                                else:  # p is ending with ".*"
                                    eli = j - 2
                                    while eli > 0:  # eliminate "a*"s after ".*"
                                        if p[eli - 1] == "*":
                                            eli -= 2
                                        else:
                                            break

                                    if eli > i:
                                        for match in range(1, i + 1):
                                            if dp[match][eli] == 1:
                                                dp[i][j] = 1
                                                break
                                            else:
                                                dp[i][j] = 0
                                    else:
                                        dp[i][j] = dp[eli][eli]
                            else:
                                k = i
                                ptr = s[k - 1]
                                while ptr == s[
                                    k - 1]:  # To find the index of 1st char. that is different from s[i-1] (in the reversed order)
                                    ptr = s[k - 1]
                                    k -= 1
                                    if k <= 0:
                                        break
                                for match in range(k, i + 1):  # like(s:aa, p:ab*a*)
                                    if dp[match][j - 2] == 1:
                                        dp[i][j] = 1
                                        break
                                    else:
                                        dp[i][j] = 0

        if dp[m][n] == 1:
            return True
        else:
            return False

