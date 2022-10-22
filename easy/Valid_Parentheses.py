"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true
"""

class Solution:
    parentheses = {
        "(":")",
        "{":"}",
        "[":"]",
    }
    def get_str(self, n:str) -> str:
        return self.parentheses.get(n)
         
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in self.parentheses:
                stack.append(i)
                
            else:
                if len(stack)==0 or self.get_str(stack.pop())!=i:
                    return False
        
        return stack == []
        
if __name__ == "__main__":
    solution = Solution()
    is_valid = lambda i : solution.isValid(i)
    print(is_valid("}}"))
    
