"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
You may return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""


# My solution
def find_repeated_dna_sequences(s: str):
    if len(s) <= 10:
        return []
    dna_set, out, out_set = set(), [], set()
    for i in range(len(s) - 9):
        dna_sequence = s[i:i + 10]
        if dna_sequence not in dna_set:
            dna_set.add(dna_sequence)
        else:
            if dna_sequence not in out_set:
                out.append(dna_sequence)
                out_set.add(dna_sequence)
    return out
