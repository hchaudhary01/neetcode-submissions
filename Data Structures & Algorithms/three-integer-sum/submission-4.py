class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        s = set()
        for n in range(len(nums)):
            if nums[n] <=0 and nums[n] not in s:
                s.add(nums[n])
                i = n+1
                j = len(nums)-1
                while i<j:
                    total = nums[i]+nums[j]+nums[n]
                    if total == 0:
                        ans.append([nums[n], nums[i], nums[j]])
                        i+=1
                        j-=1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1

                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
                            
                    elif total > 0:
                        j-=1
                    else:
                        i+=1
        return ans