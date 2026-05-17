class TimeMap:

    def __init__(self):
        self.l = dict()
        

    def set(self, key: str, value: str, time: int) -> None:
        if key in self.l:
            self.l[key].append((value, time))
        else:
            self.l[key] = [(value, time)]
        

    def get(self, key: str, time: int) -> str:
        if key not in self.l:
            return ""
        x = self.l[key]
        i, j = 0, len(x)-1
        if time>=x[-1][1]:
            return x[-1][0]
        if time<x[0][1]:
            return ""
        while i<=j:
            mid = i+(j-i)//2
            if x[mid][1]<=time:
                i = mid+1
            else:
                j = mid-1
        return x[i-1][0]
        
