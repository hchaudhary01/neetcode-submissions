class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        self.backtrack(res, temp, n, 0, 0)
        return res
    
    def backtrack(self, res, temp, n , open, close):
        if open == n and close == n:
            res.append("".join(temp.copy()))
            return 
        else:
            if close < open:
                temp.append(')')
                self.backtrack(res, temp, n, open, close+1)
                temp.pop()
            if open < n:
                temp.append('(')
                self.backtrack(res, temp, n , open+1, close)
                temp.pop()


        