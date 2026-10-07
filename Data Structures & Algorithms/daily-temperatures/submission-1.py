class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        ans = [0]*len(t)
        s = []

        for i in range(len(t)-1,-1,-1):
            while s and t[s[-1]]<=t[i]:
                s.pop()
            if not s:
                s.append(i)
                ans[i] = 0
            else:
                ans[i] = s[-1]-i
                s.append(i)
        return ans
            
            