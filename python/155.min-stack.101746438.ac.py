#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack
#
# Easy (27.61%)
# Total Accepted:    127021
# Total Submissions: 455047
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# 
# 
# pop() -- Removes the element on top of the stack.
# 
# 
# top() -- Get the top element.
# 
# 
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack = list()
        self.MinStack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.MinStack) == 0 or x <= self.MinStack[-1]:
            self.MinStack.append(x)
        self.Stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.Stack[-1] == self.MinStack[-1]:
            self.MinStack.pop()
        self.Stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.Stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.MinStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

