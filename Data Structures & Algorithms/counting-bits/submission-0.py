class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        change = 1
        for i in range(1, n+1):
            if change*2 == i:
                change = i
            ans[i] = 1+ ans[i-change]
        return ans

