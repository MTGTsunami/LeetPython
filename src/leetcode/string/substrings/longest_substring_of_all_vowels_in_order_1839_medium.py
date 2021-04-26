"""
A string is considered beautiful if it satisfies the following conditions:
Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.
Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.

Example 2:
Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.

Example 3:
Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.

Constraints:
1 <= word.length <= 5 * 105
word consists of characters 'a', 'e', 'i', 'o', and 'u'.
"""


# My solution: time O(n), space O(1)
def longest_beautiful_substring(word: str) -> int:
    if len(word) < 5:
        return 0

    substring, temp_length, stack = 0, 0, []
    char_map = {"a": None, "e": "a", "i": "e", "o": "i", "u": "o"}
    for ch in word:
        does_count = True
        if not stack:
            if ch == "a":
                stack.append("a")
                temp_length += 1
            else:
                temp_length = 0
                does_count = False
        elif stack[-1] == char_map[ch]:
            stack.append(ch)
            temp_length += 1
        elif stack[-1] == ch:
            temp_length += 1
        else:
            if ch == "a":
                temp_length = 1
                stack = ["a"]
                does_count = True
            else:
                temp_length = 0
                stack = []
                does_count = False

        if ch == "u" and does_count:
            substring = max(substring, temp_length)

    return substring


# Answer from discussion
def longest_beautiful_substring2(word: str) -> int:
    seen = set()
    lo, longest = -1, 0
    for hi, c in enumerate(word):
        if hi > 0 and c < word[hi - 1]:
            seen = set()
            lo = hi - 1
        seen.add(c)
        if len(seen) == 5:
            longest = max(longest, hi - lo)
    return longest
