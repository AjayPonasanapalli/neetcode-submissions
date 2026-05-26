class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append((current_string, num))
                current_string = ""
                num = 0

            elif ch == ']':
                prev_string, count = stack.pop()
                current_string = prev_string + count * current_string

            else:  # letter
                current_string += ch

        return current_string