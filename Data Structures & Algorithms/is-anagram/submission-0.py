class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted([s for s in s]) == sorted([s for s in t])