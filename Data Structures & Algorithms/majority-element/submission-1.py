class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr = ""
        for i in range(len(nums)):
            if count == 0:
                curr = nums[i]
                count+=1
            elif nums[i] == curr:
                count+=1
            else:
                count-=1
        return curr