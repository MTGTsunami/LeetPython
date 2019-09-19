"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        def displayThousand(a, one_num, tenToTwenty_num, tens_num):  # a must be smaller than 10000
            display = ""
            thou, remt = divmod(a, 1000)
            if thou != 0:
                display += (one_num[thou] + " Thousand")
            hund, remh = divmod(remt, 100)
            if hund != 0:
                if display:
                    display += " "
                display += (one_num[hund] + " Hundred")
            tens, remte = divmod(remh, 10)
            if tens != 0:
                if display:
                    display += " "
                if tens == 1:
                    display += (tenToTwenty_num[remte])
                else:
                    if remte != 0:
                        display += (tens_num[tens] + " " + one_num[remte])
                    else:
                        display += (tens_num[tens])
            else:
                if remte != 0:
                    if display:
                        display += " "
                    display += (one_num[remte])
            return display

        one_num = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        tenToTwenty_num = {
            0: "Ten",
            1: "Eleven",
            2: "Twelve",
            3: "Thirteen",
            4: "Fourteen",
            5: "Fifteen",
            6: "Sixteen",
            7: "Seventeen",
            8: "Eighteen",
            9: "Nineteen"
        }

        tens_num = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }

        if num == 0:
            return "Zero"

        out = ""
        bil, rembil = divmod(num, 10 ** 9)
        if bil != 0:
            out += (one_num[bil] + " Billion")
        if rembil == 0:
            return out

        mil, remmil = divmod(rembil, 10 ** 6)
        if mil != 0:
            if out:
                out += " "
            out += (displayThousand(mil, one_num, tenToTwenty_num, tens_num) + " Million")
        if remmil == 0:
            return out

        tho, remtho = divmod(remmil, 10 ** 3)
        if tho != 0:
            if out:
                out += " "
            out += (displayThousand(tho, one_num, tenToTwenty_num, tens_num) + " Thousand")
        if remtho == 0:
            return out

        if out:
            out += " "
        out += displayThousand(remtho, one_num, tenToTwenty_num, tens_num)

        return out