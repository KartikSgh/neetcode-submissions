class Solution:
    def searchMatrix(self, l: List[List[int]], t: int) -> bool:
        n, m = len(l), len(l[0])
        i, j = 0, m*n-1
        if t>=l[-1][-1]:
            if t==l[-1][-1]:
                return True
            return False
        while i<=j:
            mid = i+(j-i)//2
            if l[mid//m][mid%m]==t:
                return True
            if l[mid//m][mid%m]<t:
                i=mid+1
            else:
                j=mid-1
        return False