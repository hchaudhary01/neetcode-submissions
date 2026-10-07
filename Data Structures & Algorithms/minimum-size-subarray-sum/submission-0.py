class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        reslen = float('inf')
        res=[-1,-1]
        l = 0
        ans = 0
        for r in range(len(nums)):
            ans +=nums[r]
            #print(ans,"ans and nums[r] " ,nums[r])
            while ans>=target:
                if r-l+1<reslen:
                    reslen= r-l+1
                    res=[l,r]
                    #print(reslen, " reslen and res ", res)
                ans -= nums[l]
                l+=1
                #print( ans, " ans and nums[l] ", nums[l])
        if res[0]!=-1:
            return res[1]-res[0]+1
        else:
            return 0

