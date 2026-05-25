class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        j = 0
        while j <= i:
            if nums[j] == val:
                # move unwanted element to the end
                nums[j], nums[i] = nums[i], nums[j]
                i -= 1
            else:
                j += 1
        # new length is i+1 (everything before i is valid)
        return i + 1
