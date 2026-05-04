class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in range(1,len(nums)):
            if j!=len(nums):
                if nums[i] == nums[j]:
                    continue
                else:
                    nums[j+1] = nums[i]
                    j+=1
        return j+1
