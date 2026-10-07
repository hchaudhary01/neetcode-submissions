class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s_set = set(nums)
        if len(s_set) == len(nums):
            return False
        else:
            return True
        