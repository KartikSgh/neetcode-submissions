class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2==1:
            return False
        st = []
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            else:
                if not st:
                    return False
                x = st.pop()
                if (i==')' and x!='(') or (i=='}' and x!='{') or (i==']' and x!='['):
                    return False
        if st:
            return False
        return True

                        