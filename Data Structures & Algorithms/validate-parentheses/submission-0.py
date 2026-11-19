class Solution:
    def isValid(self, s: str) -> bool:
        seen = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                seen.append(char)
            elif char == ')' or char == '}' or char == ']':
                if len(seen) == 0:
                    return False
                if char == ')' and seen[-1] != '(':
                    return False

                elif char == '}' and seen[-1] != '{':
                    return False

                elif char == ']' and seen[-1] != '[':
                    return False

                seen.pop()

        
        return len(seen) == 0