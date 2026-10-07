class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        st =[]
        def backtrack(open,close):
            if open == n and close == n:
                ans.append("".join(st))
                return
            if open > close:
                st.append(')')
                backtrack(open,close+1)
                st.pop()
            if open<n:
                st.append('(')
                backtrack(open+1, close)
                st.pop()
            
        backtrack(0,0)
        return ans
