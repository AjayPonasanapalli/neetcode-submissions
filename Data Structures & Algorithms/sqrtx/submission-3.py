class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x//2+1
        while l<=r:
            mid = (l+r)//2
            sqr = mid*mid 
            if sqr <= x:
                l=mid+1
            else:
                r = mid-1
        return l-1