class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n+1):
            ans = ans^i
        for i in range(len(nums)):
            ans = ans^nums[i]
        return ans
