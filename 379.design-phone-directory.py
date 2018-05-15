#
# [379] Design Phone Directory
#
# https://leetcode.com/problems/design-phone-directory/description/
#
# algorithms
# Medium (36.48%)
# Total Accepted:    15.3K
# Total Submissions: 41.9K
# Testcase Example:  '["PhoneDirectory","get","get","check","get","check","release","check"]\n[[3],[],[],[2],[],[2],[2],[2]]'
#
# Design a Phone Directory which supports the following operations:
#
#
#
# get: Provide a number which is not assigned to anyone.
# check: Check if a number is available or not.
# release: Recycle or release a number.
#
#
#
# Example:
#
# // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
# PhoneDirectory directory = new PhoneDirectory(3);
#
# // It can return any available phone number. Here we assume it returns 0.
# directory.get();
#
# // Assume it returns 1.
# directory.get();
#
# // The number 2 is available, so return true.
# directory.check(2);
#
# // It returns 2, the only number that is left.
# directory.get();
#
# // The number 2 is no longer available, so return false.
# directory.check(2);
#
# // Release number 2 back to the pool.
# directory.release(2);
#
# // Number 2 is available again, return true.
# directory.check(2);
#
#
#


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.table = [True]*maxNumbers
        self.count = 0
        self.l = maxNumbers

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.count == self.l:
            return -1
        while self.count < self.l:
            if self.table[self.count]:
                break
            self.count += 1
        if self.count == self.l:
            return -1
        self.table[self.count] = False
        ret = self.count
        self.count = (self.count+1) % self.l
        return ret

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return self.table[number]

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.table[number] = True
        self.count = min(self.count, number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
