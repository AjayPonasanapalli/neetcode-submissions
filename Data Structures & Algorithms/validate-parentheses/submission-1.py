class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if stack:
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            print(stack)
        return True if len(stack) == 0 else False
        
        