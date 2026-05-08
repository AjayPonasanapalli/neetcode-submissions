class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for operation in operations:
            if operation == "+":
                ans.append(ans[-1]+ans[-2])
            elif operation == "D":
                ans.append(ans[-1]*2)
            elif operation == "C":
                ans.pop()
            else:
                ans.append(int(operation))
        return sum(ans)