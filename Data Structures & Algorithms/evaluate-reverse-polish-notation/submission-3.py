import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():  
                stack.append(int(tokens[i]))

            else:
                operator = tokens[i]
                nums2 = stack.pop()
                nums1 = stack.pop()
                if operator == "+":
                    nums1 = nums1+nums2 
                elif operator == "-":
                    nums1 = nums1-nums2 
                elif operator == "*":
                    nums1 = nums1*nums2 
                else:
                    if nums1 < 0 or nums2< 0 and not (nums1<0 and nums2<0):
                        nums1 = math.ceil(nums1/nums2)
                    else:
                        nums1 = math.floor(nums1/nums2)
                stack.append(nums1)
            print(stack)
        return stack[0]