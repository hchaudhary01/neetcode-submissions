class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        self.backtrack(res, temp, nums, target, 0, 0)
        return res
    
    def backtrack(self, res, temp, nums, target, total, start):
        if total > target:
            return
        if total == target:
            res.append(temp.copy())
            return
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(res, temp, nums, target, total+nums[i], i)
            temp.pop()
