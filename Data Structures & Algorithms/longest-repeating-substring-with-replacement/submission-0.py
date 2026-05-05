class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def fun(x):
            n = len(s)
            i, j = 0, 0
            c = 0
            ans = 0
            while j<n:
                if s[j]!=x:
                    c+=1
                if c>k:
                    while i<j:
                        if s[i]!=x:
                            c-=1
                        i+=1
                        if c==k:
                            break
                ans = max(ans, j-i+1)
                j+=1
            return ans
        l = set([i for i in s])
        ans = 0
        for i in l:
            ans = max(ans, fun(i))
        return ans

        