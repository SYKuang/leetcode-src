#
# [444] Sequence Reconstruction
#
# https://leetcode.com/problems/sequence-reconstruction/description/
#
# algorithms
# Medium (19.48%)
# Total Accepted:    10.2K
# Total Submissions: 52.5K
# Testcase Example:  '[1,2,3]\n[[1,2],[1,3]]'
#
# Check whether the original sequence org can be uniquely reconstructed from
# the sequences in seqs. The org sequence is a permutation of the integers from
# 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common
# supersequence of the sequences in seqs (i.e., a shortest sequence so that all
# sequences in seqs are subsequences of it). Determine whether there is only
# one sequence that can be reconstructed from seqs and it is the org sequence.
#
# Example 1:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
#
# Output:
# false
#
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because
# [1,3,2] is also a valid sequence that can be reconstructed.
#
#
#
# Example 2:
#
# Input:
# org: [1,2,3], seqs: [[1,2]]
#
# Output:
# false
#
# Explanation:
# The reconstructed sequence can only be [1,2].
#
#
#
# Example 3:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
#
# Output:
# true
#
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original
# sequence [1,2,3].
#
#
#
# Example 4:
#
# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
#
# Output:
# true
#
#
#
#
# UPDATE (2017/1/8):
# The seqs parameter had been changed to a list of list of strings (instead of
# a 2d array of strings). Please reload the code definition to get the latest
# changes.
#
#


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """

        """
        Solution 1:
            Create a topological graph by seqs.
            And check the topological sort with the graph
        """
        if not seqs:
            return False
        size = len(org)
        indegree = [0] * (size + 1)
        subset = [set() for _ in xrange(size + 1)]
        count = 0
        for seq in seqs:
            if len(seq) == 0:
                continue
            if any([i<1 or i>size for i in seq]):
                return False
            for i in xrange(1, len(seq)):

                if seq[i] not in subset[seq[i - 1]]:
                    indegree[seq[i]] += 1
                    subset[seq[i - 1]].add(seq[i])
            count+=1
        if not count:
            return False
        q = [i for i in org if indegree[i] == 0]
        for x in xrange(size):
            if len(q) != 1:  # more than 1 topological sort or no topological sort
                return False
            if q[0] != org[x]:  # the sequence of topological sort is not org[x]
                return False
            indegree[org[x]] -= 1
            nq = []
            for s in subset[org[x]]:
                indegree[s] -= 1
                if indegree[s] == 0:
                    nq.append(s)
            q = nq
        return True
