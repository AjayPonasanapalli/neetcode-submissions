class Solution:
    def simplifyPath(self, path: str) -> str:
        stac = path.split("/")
        stac = [el for el in stac if el != '']
        print(stac)
        ans = []
        for el in stac:
            if el == "..":
                if ans:
                    ans.pop()
            elif el == '.':
                continue
            else:
                ans.append(el)
        return "/" + "/".join(ans)