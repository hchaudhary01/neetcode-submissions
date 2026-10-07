class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        self.backtrack(res, temp, nums, 0)
        return res
    
    def backtrack(self, res, temp, nums, start):
        if len(temp) == len(nums):
            res.append(temp.copy())
        else:
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                self.backtrack(res, temp, nums, start+1)
                temp.pop()