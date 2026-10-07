class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        if l ==1:
            return nums[0]
        ans = nums[0]
        for i in range(1, l):
            ans = ans^nums[i]
        return ans