class Solution:
    def fdays(self, weights, capacity):
        days = 1
        curr_weight = 0

        for w in weights:
            if curr_weight + w <= capacity:
                curr_weight += w
            else:
                days += 1
                curr_weight = w

        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = r

        while l <= r:
            mid = (l + r) // 2

            required_days = self.fdays(weights, mid)

            if required_days <= days:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans