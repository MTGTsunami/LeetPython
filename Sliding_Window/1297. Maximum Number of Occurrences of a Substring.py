"""
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.


Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
Example 3:

Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3
Example 4:

Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0


Constraints:

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.
"""

from collections import defaultdict


class MySolution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        max_ocurrence = 0
        for size in range(minSize, maxSize + 1):
            window, strings = defaultdict(int), defaultdict(int)
            ocurr = 0
            for i in range(size):
                window[s[i]] += 1
            for i in range(len(s) - size + 1):
                if i >= 1:
                    window[s[i - 1]] -= 1
                    if window[s[i - 1]] == 0:
                        del window[s[i - 1]]
                    window[s[i + size - 1]] += 1
                if len(window) <= maxLetters:
                    strings[s[i:i + size]] += 1
            max_ocurrence = max(max_ocurrence, max(strings.values()) if len(strings.values()) != 0 else 0)
        return max_ocurrence


