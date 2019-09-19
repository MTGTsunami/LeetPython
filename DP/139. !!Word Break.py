from queue import Queue
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

# 按位循环s不要循环wordDict！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
class MyNaiveSolution(object):  # case 28 TLE
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        checkstr = s.replace("#", "")
        if not checkstr.isalpha():
            return True

        for word in wordDict:
            if word in s:
                temp = s.replace(word, "#", 1)
                flag = self.wordBreak(temp, wordDict)
                if flag:
                    return True
        return False


class SolutionBFS(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        wordDictSet = set(wordDict)
        queue = Queue()
        visited = [0] * n
        queue.put(0)

        while not queue.empty():
            start = queue.get()
            if visited[start] == 0:
                for end in range(start + 1, n + 1):
                    if s[start: end] in wordDictSet:
                        queue.put(end)
                        if end == n:
                            return True
                visited[start] = 1
        return False


"""
The intuition behind this approach is that the given problem (s) can be divided into subproblems s1 and s2. 
If these subproblems individually satisfy the required conditions, the complete problem, s also satisfies the same. 
e.g. "catsanddog" can be split into two substrings "catsand", "dog". 
The subproblem "catsand" can be further divided into "cats","and", 
which individually are a part of the dictionary making "catsand" satisfy the condition. 
Going further backwards, "catsand", "dog" also satisfy the required criteria individually leading to the complete string "catsanddog" also to satisfy the criteria.

Now, we'll move onto the process of dp array formation. We make use of dp array of size n+1, where n is the length of the given string.
We also use two index pointers i and j, where i refers to the length of the substring (s') considered currently starting from the beginning, 
and j refers to the index partitioning the current substring (s') into smaller substrings s'(0,j)and s'(j+1,i).
To fill in the dp array, we initialize the element dp[0] as true, since the null string is always present in the dictionary, 
and the rest of the elements of dp as }false. 
We consider substrings of all possible lengths starting from the beginning by making use of index ii. 
For every such substring, we partition the string into two further substrings s1'and s2' in all possible ways using the index j
(Note that the i now refers to the ending index of s2').
Now, to fill in the entry dp[i], we check if the dp[j] contains true, 
i.e. if the substring s1'fulfills the required criteria. 
If so, we further check if s2'is present in the dictionary. 
If both the strings fulfill the criteria, we make dp[i] as true, otherwise as false.
"""


class SolutionDP(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        wordDictSet = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and s[j: i] in wordDictSet:
                    dp[i] = True
                    break
        return dp[-1]