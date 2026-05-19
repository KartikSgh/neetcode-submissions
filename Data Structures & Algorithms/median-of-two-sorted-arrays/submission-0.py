class Solution:
    def findMedianSortedArrays(self, l1: List[int], l2: List[int]) -> float:
        n, m = len(l1), len(l2)
        def fun(l1, l2, k):
            n, m = len(l1), len(l2)
            if n==0:
                return l2[k-1]
            if m==0:
                return l1[k-1]
            if k==1:
                return min(l1[0], l2[0])
            i, j = min(n, k//2), min(m, k//2)
            if l1[i-1]<l2[j-1]:
                return fun(l1[i:], l2, k-i)
            else:
                return fun(l1, l2[j:], k-j)
        if (n+m)%2==0:
            return (fun(l1, l2, (n+m)//2)+fun(l1, l2, (n+m)//2+1))/2
        else:
            return fun(l1, l2, (n+m)//2+1)

