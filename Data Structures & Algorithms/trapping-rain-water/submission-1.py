class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix=[0]*n
        sufix = [0]*n
        prefix[0] = height[0]
        sufix[n-1]=height[n-1]

        ans = 0
        for i in range(1,n):
            prefix[i]= max(height[i], prefix[i-1])
        
        #print(prefix)
        for i in range(n-2, -1,-1):
            sufix[i] = max(height[i], sufix[i+1])
        
        
        #print(sufix)
        for i in range(n):
            ans += min(prefix[i], sufix[i])-height[i]
            #print(ans, prefix[i], sufix[i], height[i])
        return ans