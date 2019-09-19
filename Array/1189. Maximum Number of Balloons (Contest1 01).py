"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

"""


class MySolution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        d = {"a": 0, "b": 0, "l": 0, "o": 0, "n": 0}
        for ch in text:
            if ch == "a" or ch == "b" or ch == "l" or ch == "o" or ch == "n":
                d[ch] += 1
        d["o"] /= 2
        d["l"] /= 2

        maxq = min(d.values())
        return maxq
