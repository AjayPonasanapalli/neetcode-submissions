class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero,two = 0,len(nums)-1
        i=0
        while i<=two:
            if nums[i] == 0:
                nums[zero],nums[i] = nums[i],nums[zero]
                zero+=1
            elif nums[i] == 2:
                nums[i],nums[two] = nums[two],nums[i]
                two-=1
                i-=1
            i+=1
        