#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees
#
# algorithms
# Medium (41.30%)
# Total Accepted:    135K
# Total Submissions: 325.7K
# Testcase Example:  '1'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1...n?
#
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n<2:
            return 1
        count=[0 for _ in xrange(n+1)]
        count[0]=1
        count[1]=1
        for i in xrange(2,n+1):
            for j in xrange(0,i):
                count[i]=count[i]+count[j]*count[i-j-1]

        return count[n]
