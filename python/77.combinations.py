#
# [77] Combinations
#
# https://leetcode.com/problems/combinations
#
# Medium (39.78%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '4\n2'
#
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
#
#
# For example,
# If n = 4 and k = 2, a solution is:
#
#
#
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        table=[i for i in xrange(1,n+1)]
        return self.helper(table,k)
    def helper(self,table,k):
        ret=[]
        if len(table)<k or k==0:
            return None
        elif k==1:
            for n in table:
                ret.append([n])
            return ret
        for i in xrange(len(table)-1):
            tmp=self.helper(table[i+1:],k-1)
            if tmp:
                for r in tmp:
                    r.insert(0,table[i])
                    ret.append(r)
        if len(ret)>0:
            return ret
        else:
            return None
