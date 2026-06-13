class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return True
            elif nums[l]==nums[r]:
                if nums[l]==target:
                    return True
                else:
                    l+=1
                    r-=1
                    continue
            elif nums[l]<=nums[mid]:
                if nums[l]>target or target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return False