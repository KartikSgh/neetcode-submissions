import math
class Solution:
    def minEatingSpeed(self, l: List[int], h: int) -> int:
        n = len(l)
        if h==n:
            return max(l)
        i, j = 1, max(l)
        def fun(mid):
            ans = 0
            for i in l:
                ans+=math.ceil(i/mid)
            if ans<=h:
                return True
            return False
        while i<=j:
            mid = i+(j-i)//2
            if fun(mid):
                j = mid-1
            else:
                i = mid+1
        return j+1