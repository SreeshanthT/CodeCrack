class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        extended_list = nums1.copy()
        extended_list.extend(nums2)
        extended_list.sort()
        
        if len(extended_list) and len(extended_list) % 2 == 1:
            index = len(extended_list)//2 
            return extended_list[index]
            
        if len(extended_list) and len(extended_list) % 2 == 0:
            index_1 = (len(extended_list))//2 -1
            index_2 = index_1 + 1
            return (extended_list[index_1] + extended_list[index_2])/2
            
            
            
        
        
        
if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2,4]
    solution = Solution()
    solution.findMedianSortedArrays(nums1,nums2)