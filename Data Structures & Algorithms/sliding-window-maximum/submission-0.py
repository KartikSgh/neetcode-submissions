import heapq
class Solution:
    def maxSlidingWindow(self, l: List[int], k: int) -> List[int]:
        n = len(l)
        if n==k:
            return [max(l)]
        if k==1:
            return l
        h = []
        ans = []
        for i in range(n):
            heapq.heappush(h, (-l[i], i))
            if i>=k-1:
                mval = float('-inf')
                while h:
                    if h[0][1]>i-k:
                        mval = -h[0][0]
                        break
                    else:
                        heapq.heappop(h)
                ans.append(mval)
        return ans
                        
