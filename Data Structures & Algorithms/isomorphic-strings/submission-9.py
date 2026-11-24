class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i]
            else:
                if t[i] != dic[s[i]]:
                    return False
        
        
        return len(dic) == len(set(dic.values()))
            
        