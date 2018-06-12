#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (33.33%)
# Total Accepted:    97.3K
# Total Submissions: 291.7K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
#
# Example:
#
#
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
#
#
#


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<10:
            return []
        res = set()
        table = set()
        maping = {'A': 0, 'T': 1, "C": 2, "G": 3}
        i = 0
        cur = 0
        while i < 9:
            cur = cur << 2 | maping[s[i]]
            i += 1
        while i < len(s):
            cur = (cur & 0x3ffff)<< 2 | maping[s[i]]
            if cur in table:
                res.add(s[i-9:i+1])
            else:
                table.add(cur)
            i+=1
        return list(res)
