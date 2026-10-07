class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorel = nums[0]
        count=0
        for i in range(len(nums)):
            if nums[i]== majorel:
                count+=1
            if count==0:
                majorel = nums[i+1]
            if nums[i]!=majorel:
                count-=1
        return majorel