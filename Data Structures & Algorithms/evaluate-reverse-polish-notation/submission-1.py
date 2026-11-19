class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = []
        for char in tokens:
            if char == "+":
                b = seen.pop()
                a = seen.pop()
                seen.append(a + b)

            elif char == "*":
                b = seen.pop()
                a = seen.pop()
                seen.append(a * b)

            elif char == "-":
                b = seen.pop()
                a = seen.pop()
                seen.append(a - b)

            elif char == "/":
                b = seen.pop()
                a = seen.pop()
                seen.append(int(a / b))

            else:
                seen.append(int(char))

        return seen[-1]