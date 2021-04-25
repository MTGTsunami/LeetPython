"""
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
"""

from collections import *


class MySolution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack, elements = [formula[0]], defaultdict(int)
        rightPar = False
        count = ""
        for i, ch in enumerate(formula[1:]):
            if not rightPar:
                if ch.islower():
                    stack[-1] += ch
                elif ch.isdigit():
                    if stack[-1].isdigit():
                        stack[-1] += ch
                    else:
                        stack.append(ch)
                elif ch == ')':
                    if stack[-1].isalpha():
                        stack.append("1")
                    rightPar = True
                else:
                    if stack[-1].isalpha():
                        stack.append("1")
                        stack.append(ch)
                    else:
                        stack.append(ch)

            else:
                if ch.isdigit():
                    count += ch
                    if i + 2 >= len(formula) or not formula[i + 2].isdigit():
                        count = int(count)
                        j = len(stack) - 1
                        while stack[j] != '(':
                            if stack[j].isdigit():
                                stack[j] = int(stack[j])
                                stack[j] *= count
                                stack[j] = str(stack[j])
                            j -= 1
                        stack[j] = '#'
                        count = ""
                        rightPar = False
                else:
                    j = len(stack) - 1
                    while stack[j] != '(':
                        j -= 1
                    stack[j] = '#'
                    stack.append(ch)
                    rightPar = False

        if stack[-1].isalpha():
            stack.append("1")
        i = 0
        while i < len(stack):
            if stack[i] != '#':
                elements[stack[i]] += int(stack[i + 1])
                i += 1
            i += 1
        out = ""
        for k, v in sorted(elements.items(), key=lambda x: x[0]):
            out += k
            if int(v) != 1:
                out += str(v)
        return out


class Solution(object):  # Brilliant!!!
    def countOfAtoms(self, formula):
        N = len(formula)
        stack = [Counter()]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start: i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                stack[-1][name] += multiplicity

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))


