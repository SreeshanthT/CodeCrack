"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)<=0:
            return ""

        if len(strs)==1:
            return strs[0]
        
        longPrefix = ''
        i=0
        p=0
        count = lambda i : len(min(i, key=len)) - 1
        
        while True:
            if i > count(strs):
                return longPrefix

            for j in range(1,len(strs)):
                if len(strs[j]) > i and strs[0][i] == strs[j][i]:
                    p += 1
                    if p == (len(strs) - 1):
                        longPrefix += strs[0][i]
                        p=0
                else:
                    return longPrefix    
            i += 1
            
            
        
        

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    solutution = Solution()
    longPrefix = solutution.longestCommonPrefix(strs)
    print(longPrefix)