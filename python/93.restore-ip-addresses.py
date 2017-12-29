#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses
#
# algorithms
# Medium (27.64%)
# Total Accepted:    93.7K
# Total Submissions: 337K
# Testcase Example:  '"0000"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
#
#
# For example:
# Given "25525511135",
#
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#
#
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        self.ret=[]
        self.helper(s,0,[])
        return self.ret
    def helper(self,s,index,ip):
        if index==len(s):
            if len(ip)==4:
                sIp=ip[0]
                for i in xrange(1,4):
                    sIp=sIp+"."+ip[i]
                self.ret.append(sIp)
            return
        for i in xrange(index+1,index+4):
            if i <=len(s):
                num=s[index:i]
                if self.isVaild(num):
                    ip.append(num)
                    self.helper(s,i,ip)
                    ip.pop()
            else:
                break
    def isVaild(self,num):
        if len(num)>1 and num[0]=='0':
            return False
        elif int(num) <=255 and int(num) >=0:
            return True
        else:
            return False


