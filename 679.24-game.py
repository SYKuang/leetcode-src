#
# [679] 24 Game
#
# https://leetcode.com/problems/24-game/description/
#
# algorithms
# Hard (38.86%)
# Total Accepted:    7.9K
# Total Submissions: 20.4K
# Testcase Example:  '[4,1,8,7]'
#
#
# You have 4 cards each containing a number from 1 to 9.  You need to judge
# whether they could operated through *, /, +, -, (, ) to get the value of
# 24.
#
#
# Example 1:
#
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#
#
#
# Example 2:
#
# Input: [1, 2, 1, 2]
# Output: False
#
#
#
# Note:
#
# The division operator / represents real division, not integer division.  For
# example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use -
# as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression
# -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2,
# 1, 2], we cannot write this as 12 + 12.
#
#
#
#


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.ret = False
        nums = [float(n) for n in nums]
        self.helper(nums)
        return self.ret

    def helper(self, nums):
        if self.ret:
            return
        if len(nums) == 1:
            if 24-1e-3 < nums[0] < 24+1e-3:
                self.ret = True
            return
        l = len(nums)
        for i in xrange(l-1):
            for j in xrange(i+1, l):
                rest = [nums[k] for k in xrange(l) if k != i and k != j]
                a, b = nums[i], nums[j]
                for oper in ("+", "-", "*", "/"):
                    if oper == "/":
                        if b != 0:
                            rest.append(a/b)
                            self.helper(rest)
                            if self.ret:
                                return
                            rest.pop()
                        if a == 0:
                            continue
                        rest.append(b/a)
                    elif oper == "+":
                        rest.append(a+b)
                    elif oper == "-":
                        rest.append(a-b)
                        self.helper(rest)
                        if self.ret:
                            return
                        rest.pop()
                        rest.append(b-a)
                    elif oper == "*":
                        rest.append(a*b)
                    self.helper(rest)
                    if self.ret:
                        return
                    rest.pop()
        return
