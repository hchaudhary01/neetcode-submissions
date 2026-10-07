class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if not st or s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])
            else:
                if s[i]==')' and st[-1] == '(':
                    st.pop()
                elif s[i] == '}' and st[-1] == '{':
                    st.pop()
                elif s[i]==']' and st[-1] == '[':
                    st.pop()
                else:
                    st.append(s[i])
        return True if len(st)==0 else False
