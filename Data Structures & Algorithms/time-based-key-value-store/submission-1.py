class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = sorted(self.time[key], key=lambda x: x[1])
        l,r = 0,len(timestamps)-1
        ans =""
        while l<=r:
            mid = (l+r)//2
            if timestamps[mid][1] == timestamp:
                return timestamps[mid][0]
            elif timestamps[mid][1]<timestamp:
                ans = timestamps[mid][0]
                l = mid+1
            else:
                r=mid-1
        return ans

