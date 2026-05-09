class Solution:
    def dailyTemperatures(self, l: List[int]) -> List[int]:
        n = len(l)
        ans = [0 for i in range(n)]
        s = [(l[-1], n-1)]
        for i in range(n-2, -1, -1):
            while s and s[-1][0]<=l[i]:
                s.pop()
            if s:
                ans[i] = s[-1][1]-i
            s.append((l[i], i))
        return ans
