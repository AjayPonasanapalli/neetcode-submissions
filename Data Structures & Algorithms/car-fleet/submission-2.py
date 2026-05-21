class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [[position[i],(target-position[i])/speed[i]] for i in range(len(position))]
        time.sort(key=lambda x: x[0])
        print(time)
        ans = 1
        for i in range(len(time)-2,-1,-1):
            if time[i][1]<time[i+1][1]:
                time[i][1] = time[i+1][1]
        print(time)
        ans_set = set()
        for i in range(len(time)):
            ans_set.add(time[i][1])
        return len(ans_set)