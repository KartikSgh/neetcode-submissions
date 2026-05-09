import math
class Solution:
    def evalRPN(self, l: List[str]) -> int:
        s = []
        for i in l:
            if i=='+' or i=='-' or i=='*' or i=='/':
                if i=='/':
                    b = s.pop()
                    a = s.pop()
                    if a*b>=0:
                        s.append(a//b)
                    else:
                        s.append(math.ceil(a/b))
                if i=='+':
                    s.append(s.pop()+s.pop())
                if i=='-':
                    s.append(-s.pop()+s.pop())
                if i=='*':
                    s.append(s.pop()*s.pop())
            else:
                s.append(int(i))
        return s[0]
        