#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (53.29%)
# Total Accepted:    24.2K
# Total Submissions: 45.5K
# Testcase Example:  '2'
#
#
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as
# an array that is constructed by these N numbers successfully if one of the
# following is true for the ith position (1
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
#
#
#
#
# Now given N, how many beautiful arrangements can you construct?
#
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation:
# The first beautiful arrangement is [1, 2]:
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# The second beautiful arrangement is [2, 1]:
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
#
#
#
# Note:
#
# N is a positive integer and will not exceed 15.
#
#
#


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.mem = {}
        self.res = 0
        self.a = [{j for j in range(1, N+1) if i %
                   j == 0 or j % i == 0} for i in range(1, N+1)]
        self.a.sort(key=len)
        return self.helper(0,frozenset())
    def helper(self, pos, visited):
        if pos == len(self.a):
            return 1
        counter = 0
        for i in self.a[pos]:
            if i not in visited:
                newVisited = visited | {i}
                if newVisited not in self.mem:
                    self.mem[newVisited] = self.helper(pos+1, newVisited)
                counter += self.mem[newVisited]
        return counter
