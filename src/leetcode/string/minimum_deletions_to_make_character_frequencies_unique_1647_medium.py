"""
A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.
The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.


Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).


Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
"""


# My solution
def min_deletions1(s: str) -> int:
    from collections import Counter
    count_char = list(Counter(s).values())
    count_frequency = Counter(count_char)
    out = 0
    frequency_set = set(count_frequency.keys())
    for count, freq in count_frequency.items():
        pre_minus = 0
        while freq != 1:
            step = count
            step -= pre_minus
            times = 0
            while step in frequency_set:
                step -= 1
                times += 1
            pre_minus += times
            out += pre_minus
            if step != 0:
                frequency_set.add(step)
            freq -= 1
    return out


def min_deletions2(s: str) -> int:
    import collections
    cnt, res, used = collections.Counter(s), 0, set()
    for ch, freq in cnt.items():
        while freq > 0 and freq in used:
            freq -= 1
            res += 1
        used.add(freq)
    return res
