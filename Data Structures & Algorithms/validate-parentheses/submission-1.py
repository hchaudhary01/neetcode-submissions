class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c== '{' or c== '[':
                st.append(c)
                #print("stack", st)
            else:
                if c == ')' and st and st[-1] == '(':
                    st.pop()
                elif c == '}' and st and st[-1] == '{':
                    st.pop()
                elif c == ']' and st and st[-1] == '[':
                    #print("stack in elif", st)
                    st.pop()
                    #print("stack in elif after", st)
                else:
                    st.append(c)
        if len(st)==0:
            return True
        else:
            return False
                

        