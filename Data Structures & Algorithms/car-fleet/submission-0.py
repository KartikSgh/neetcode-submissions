class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        n = len(p)
        l = [(p[i], s[i]) for i in range(n)]
        l.sort(reverse=True)
        prev = 0
        ans = 0
        for i in range(n):
            time = (t-l[i][0])/l[i][1]
            if time>prev:
                ans+=1
                prev = time
        return ans
