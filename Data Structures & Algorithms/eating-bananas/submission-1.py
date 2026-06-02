class Solution:
    def num_piles(self,piles,r):
        hours = 0
        for ele in piles:
            if ele%r == 0:
                hours+=ele//r 
            else:
                hours += ((ele//r) +1)
        return hours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 0,max(piles)
        if h == len(piles):
            return max(piles)
        while l<=r:
            mid = (l+r)//2
            if mid>0:
                hours = self.num_piles(piles,mid)
            else:
                break
            if hours <= h:
                ans = mid
                r=mid-1
            else:
                l = mid+1

        return ans