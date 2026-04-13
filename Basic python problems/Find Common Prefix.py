class Solution(object):
    def longestCommonPrefix(self, strs):
       for i in range(len(strs[0])):
          for strs in strs[1:]:
             if len(strs)<=i or s[i] != strs[0][i]:
                return strs[0][:i]
     return strs[0]
