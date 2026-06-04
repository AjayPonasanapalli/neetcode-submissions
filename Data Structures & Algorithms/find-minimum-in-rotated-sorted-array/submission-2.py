class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        ans=float('inf')
        while l<=r:
            if l==r:
                return nums[l]
            
            mid = (l+r)//2
            if mid>0 and nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                return nums[mid]
            
            elif nums[l]>nums[mid]:
                if nums[r]<=nums[mid]:
                    ans = mid 
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[l]<nums[r]:
                    r=mid-1
                    ans=mid
                else:
                    l=mid+1


        return nums[ans]
