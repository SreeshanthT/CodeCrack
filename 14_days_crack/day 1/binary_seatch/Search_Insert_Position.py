class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)
    
if __name__ == "__main__":
    solution = Solution()
    solution.searchInsert([1,3,5,6], 5)