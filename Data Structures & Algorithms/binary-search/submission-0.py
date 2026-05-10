class Solution:
    def search(self, l: List[int], t: int) -> int:
        n = len(l)
        if n==1:
            if l[0]==t:
                return 0
            return -1
        if t>=l[-1]:
            if l[-1]==t:
                return n-1
            return -1
        i, j = 0, n-1
        while i<=j:
            mid = int(i+(j-i)/2)
            if l[mid]==t:
                return mid
            if l[mid]>t:
                j=mid-1
            else:
                i=mid+1
        return -1