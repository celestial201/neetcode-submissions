class Solution:
    def calPoints(self, operations: List[str]) -> int:
        seen = []

        for char in operations:

            if char == "C":
                seen.pop()

            elif char == "D":
                seen.append(seen[-1] * 2)

            elif char == "+":
                seen.append(seen[-1] + seen[-2])

            else:
                seen.append(int(char))

        return sum(seen)