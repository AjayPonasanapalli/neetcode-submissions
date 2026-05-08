class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l, r = 0, 0
        ans = 0
        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                print(hash_set, "remove", s[r])
                l += 1
            hash_set.add(s[r])
            print(hash_set, "adding")
            ans = max(ans, len(hash_set))

        return ans
