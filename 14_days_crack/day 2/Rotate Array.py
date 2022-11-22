class Solution(object):
    def rotate(self, nums, k):

        i = 0
        while i < k:
            if nums[-1] > 0:
                nums = nums[-1:]+nums[:-1]
            i += 1
        return nums
    
    def rotate1(self, nums, k):
        
        index = k%len(nums)
        print(k)
        print(len(nums))
        print(index)
        nums[:] = nums[-index:]+nums[:-index]
        return nums
        
if __name__ == "__main__":
    solution = Solution()
    a = solution.rotate1(nums=[1,2],k=3)
    # b = solution.rotate(nums=[-1,-100,3,99],k=2)
    print(a)