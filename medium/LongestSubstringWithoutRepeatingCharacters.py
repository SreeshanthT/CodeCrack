class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        actual_list = []
        subtitute = []
        temp_list = []
        
        
        if len(s) <= 1:
            return len(s)
        
        for i in s:
            if i in temp_list:
                subtitute = temp_list.copy()
                if len(subtitute) >= len(actual_list):
                    actual_list = subtitute.copy()
                    subtitute.clear()
                temp_list.clear()
            temp_list.append(i)
             
        if len(temp_list) > 0:
            actual_list = temp_list.copy()
         
        return len(actual_list)
    

if __name__ == "__main__":
    solution = Solution()
    # print(solution.lengthOfLongestSubstring("abcabcbb"))
    # print(solution.lengthOfLongestSubstring("bbbbb"))
    # print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring(" "))
    print(solution.lengthOfLongestSubstring("aua"))