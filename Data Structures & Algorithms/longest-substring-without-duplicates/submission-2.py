class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            hash_set = set()
            for r in range(i,len(s)):
                if s[r] in hash_set:
                    break
                hash_set.add(s[r])
            ans = max(len(hash_set),ans)
                
        return ans