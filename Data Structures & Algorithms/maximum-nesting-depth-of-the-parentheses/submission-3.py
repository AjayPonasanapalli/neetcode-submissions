class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        opens = 0
        for i in range(len(s)):
            if s[i] == '(':
                opens+=1
                ans = max(ans,opens)
            elif s[i]==')':
                opens-=1
        return ans
        