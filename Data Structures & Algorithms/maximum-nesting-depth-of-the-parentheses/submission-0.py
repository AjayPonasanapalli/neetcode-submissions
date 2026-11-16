class Solution:
    def maxDepth(self, s: str) -> int:
        stac = []
        ans = 0
        for i in range(len(s)):
            if s[i] not in ['(',')']:
                continue
            else:

                if s[i] == ')':
                    print(i)
                    stac.pop()
                else:
                    stac.append('(')
                    ans = max(ans,len(stac))
        return ans


        
        