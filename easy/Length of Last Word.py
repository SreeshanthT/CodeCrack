"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s.strip())
        a = s.split(" ")
        a.reverse()
        for i,v in enumerate(a):
            if len(v) > 0: return(len(v))
            
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
                
    
if __name__ == "__main__":
    solution = Solution()
    a = solution.lengthOfLastWord(s="   fly me   to   the moon  ")
    print(a)