class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort()
        self.backtrack(res, temp, candidates, target, 0, 0)
        return res
    
    def backtrack(self, res, temp, c, target, total, start):
        if total > target:
            return
        if target == total:
            res.append(temp.copy())
            return

        for i in range(start, len(c)):
            if i > start and c[i]==c[i-1]:
                continue
            temp.append(c[i])
            self.backtrack(res,temp, c, target, total+c[i], i+1)
            temp.pop()
