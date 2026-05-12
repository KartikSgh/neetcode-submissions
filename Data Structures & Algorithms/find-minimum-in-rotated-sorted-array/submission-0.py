class Solution:
    def findMin(self, l: List[int]) -> int:
        n = len(l)
        if n==1:
            return l[0]
        if l[0]<l[-1]:
            return l[0]
        i, j = 1, n-1
        while i<=j:
            mid = i+(j-i)//2
            if l[mid]<l[0]:
                j = mid-1
            else:
                i=mid+1
        return l[i]


        