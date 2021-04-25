"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""


class Solution1(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m < n:
            n = n & (n - 1)
        return n


class Solution2(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i


"""
The key point: reduce n by removing the rightest '1' bit until n<=m;

(1)if n>m,suppose m = yyyzzz, n = xxx100, because m is less than n, m can be equal to three cases:

(a) xxx011 (if yyy==xxx)
(b) less than xxx011 (if yyy==xxx)
(c) yyyzzz (if yyy<xxx)
for case (a), and (b), xxx011 will always be ANDed to the result, which results in xxx011 & xxx100 = uuu000(uuu == yyy&xxx == xxx);

for case (c), xxx000/xxx011 will always be ANDed to the result, which results in yyyzzz & xxx000 & xxx011 & xxx100 = uuu000 (uuu <= yyy & xxx)

=> for any case, you will notice that: rangBitWiseAnd(vvvzzz,xxx100) == uuu000 == rangBitWiseAnd(vvvzzz,xxx000), (not matter what the value of"uuu" will be, the last three digits will be all zero)

=> This is why the rightest '1' bit can be removed by : n = n & (n-1);

(2)when n==m, obviously n is the result.

(3)when n < m, suppose we reduce n from rangBitWiseAnd(yyyzzz,xxx100) to rangBitWiseAnd(yyyzzz,xxx000);

i) xxx100 >yyyzzz => xxx >= yyy;

ii) xxx000 < yyyzzz => xxx <= yyy;

=> xxx == yyy;

=> rangBitWiseAnd(yyyzzz,xxx000) == rangeBitWiseAnd(xxxzzz,xxx000);

=>result is xxx000, which is also n;
"""
