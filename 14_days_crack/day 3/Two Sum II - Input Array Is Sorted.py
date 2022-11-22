"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:
    
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index_list = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target: index_list += [i+1,j+1]
                    
        return index_list
    
    def twoSum1(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers)-1
        
        while l != r:
            
            if numbers[r] + numbers[l] == target: return [l+1, r+1]
            
            if numbers[r] + numbers[l] > target: r -= 1
            else: l += 1
            
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left != right:
            if numbers[right] + numbers[left] == target:
                return [left+1,right+1] 
            elif numbers[right] + numbers[left] > target:
                right -= 1
            else: 
                left += 1
    
        
if __name__ == "__main__":
    solution = Solution()
    a = solution.twoSum2([2,7,11,15],9)
    print(a)