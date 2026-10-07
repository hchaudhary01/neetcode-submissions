class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in s:
                count =1
                while i+1 in s:
                    count+=1
                    i+=1
                ans = max(ans, count)
        return ans
