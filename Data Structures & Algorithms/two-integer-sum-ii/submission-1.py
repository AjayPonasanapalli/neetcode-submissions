# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         ans_dict = defaultdict(int)
#         for i in range(len(numbers)):
#             tmp = target - numbers[i]
#             if ans_dict[tmp]:
#                 return [ans_dict[tmp],i+1]
#             ans_dict[numbers[i]] = i+1
#         return []

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []