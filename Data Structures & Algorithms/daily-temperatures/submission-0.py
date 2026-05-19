class Solution:
    def dailyTemperatures(self, temperatures: List[int]):
        result = [0]*len(temperatures)
        stack = [(temperatures[0],0)]
        for i in range(1,len(temperatures)):
            if stack[-1][0]>temperatures[i]:
                stack.append((temperatures[i],i))
            else:
                while stack and stack[-1][0]<temperatures[i]:
                    temp,index = stack.pop()
                    result[index] = i-index
                stack.append((temperatures[i],i))
        return result                           
            