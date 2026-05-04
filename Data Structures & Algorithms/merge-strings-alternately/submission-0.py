class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        ans =[]
        while i<len(word1) and j<len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1

        if i == len(word1):
            for k in range(j,len(word2)):
                ans.append(word2[k])
        else:
              for k in range(i,len(word1)):
                ans.append(word1[k])
        return "".join(ans)