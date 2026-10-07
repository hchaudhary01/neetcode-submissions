class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_set = set(nums)
        ans = 0
        #find smallest number in set first
        #then find if the next numbers exissts in the set and find the length
        for i in nums:
            if i-1 not in s_set:
                count = 1
                while i+1 in s_set:
                    count+=1
                    i+=1
                ans = max(ans, count)
        return ans
        