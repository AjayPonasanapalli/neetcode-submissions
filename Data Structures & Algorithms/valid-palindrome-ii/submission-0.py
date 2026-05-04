def is_palindrome(s):
    return s==s[::-1]

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                if is_palindrome(s[i+1:j+1]) or is_palindrome(s[i:j]):
                    return True
                else:
                    return False
        return True