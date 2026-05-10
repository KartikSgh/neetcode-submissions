class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        n = len(h)
        t = [0 for i in range(n)]
        s = [(-1, n)]
        for i in range(n-1, -1, -1):
            while s and s[-1][0]>=h[i]:
                s.pop()
            t[i]=s[-1][1]
            s.append((h[i], i))
        s = [(-1, -1)]
        ans = 0
        for i in range(n):
            while s and s[-1][0]>=h[i]:
                s.pop()
            ans = max(ans, h[i]*(t[i]-s[-1][1]-1))
            s.append((h[i], i))
        return ans