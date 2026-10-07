class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()
        self.backtrack(res,temp,nums,0)
        return res
    
    def backtrack(self, res, temp, nums, start):
        res.append(temp.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.backtrack(res, temp, nums, i+1)
            temp.pop()
        