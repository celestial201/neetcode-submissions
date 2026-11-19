class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = []

        for char in tokens:

            if char not in ["+", "-", "*", "/"]:
                seen.append(int(char))

            else:
                b = seen.pop()
                a = seen.pop()

                if char == "+":
                    seen.append(a + b)

                elif char == "-":
                    seen.append(a - b)

                elif char == "*":
                    seen.append(a * b)

                elif char == "/":
                    seen.append(int(a / b))

        return seen[-1]