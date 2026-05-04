# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         j=0
#         for i in range(1,len(nums)):
#             if j!=len(nums):
#                 if nums[i] == nums[j]:
#                     continue
#                 else:
#                     nums[j+1] = nums[i]
#                     j+=1
#         return j+1


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
