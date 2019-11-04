"""
Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.

For example, 12321 is a palindrome.



Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101


Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""


class MySolution:  # brutal force with math shortcut
    def primePalindrome(self, N: int) -> int:
        while not self.isPalindrome(N) or not self.isPrime(N):
            N += 1
            # There are no prime palindromes between 10^7 and 10^8
            # ∑i=0to3 ai(10^(7−i)+10^i)≡∑ai((−1)^(7−i)+(−1)^i)≡∑a(0)≡0 mod 11
            if 10 ** 7 <= N < 10 ** 8:
                N = 10 ** 8
        return N

    def isPalindrome(self, N):
        N = str(N)
        r = len(N) // 2
        l = r if len(N) % 2 == 1 else r - 1
        while r < len(N):
            if N[l] != N[r]:
                return False
            r += 1
            l -= 1
        return True

    def isPrime(self, N):
        if N == 1:
            return False
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                return False
        return True


class Solution:
    # Generate Palindromes
    def primePalindrome(self, N: int) -> int:
        def is_prime(n):
            return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))

        for length in range(1, 6):
            # Check for odd-length palindromes
            for root in range(10 ** (length - 1), 10 ** length):
                s = str(root)
                x = int(s + s[-2::-1])  # eg. s = '123' to x = int('12321')
                if x >= N and is_prime(x):
                    return x
                    # If we didn't check for even-length palindromes:
                    # return min(x, 11) if N <= 11 else x

            # Check for even-length palindromes
            for root in range(10 ** (length - 1), 10 ** length):
                s = str(root)
                x = int(s + s[-1::-1])  # eg. s = '123' to x = int('123321')
                if x >= N and is_prime(x):
                    return x


