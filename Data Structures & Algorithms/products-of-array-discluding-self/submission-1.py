class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]* len(nums)
        pre = [0]* len(nums)
        suf = [0]* len(nums)

        pre[0] = suf[len(nums)-1] = 1
        for i in range(1, len(nums)):
            pre[i]=nums[i-1]*pre[i-1]

        for j in range(len(nums)-2, -1,-1):
            suf[j]=suf[j+1]*nums[j+1]

        for i in range(len(nums)):
            res[i] = pre[i]*suf[i]
        return res