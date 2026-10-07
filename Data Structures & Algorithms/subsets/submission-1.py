class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        self.backtrack(res,temp,nums,0)
        return res

    def backtrack(self, res, temp, nums, start):
        res.append(temp.copy())
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(res,temp,nums,i+1)
            temp.pop()