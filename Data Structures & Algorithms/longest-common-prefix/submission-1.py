class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort(key=lambda s: len(s))
        print(strs)
        prefix = strs[0]
        i = 0
        while i<len(prefix):
            broke = 0
            for el in strs[1:]:
                if el[i]!=prefix[i]:
                    broke = 1
                    break
            if not broke:
                i+=1
            else:
                break
        return prefix[:i]
        
