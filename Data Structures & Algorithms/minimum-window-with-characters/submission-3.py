class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = {}
        window = {}

        left = 0
        have = 0

        min_len = float('inf')
        start = 0

        # Step 1: Count frequencies of characters in t
        for char in t:
            need[char] = 1 + need.get(char, 0)

        required = len(need)

        # Step 2: Expand the sliding window
        for right in range(len(s)):

            window[s[right]] = 1 + window.get(s[right], 0)

            # Step 3: Check if required frequency is satisfied
            if s[right] in need:
                if window[s[right]] == need[s[right]]:
                    have += 1

            # Step 4: Shrink the window
            while have == required:

                length = right - left + 1

                # Update minimum window
                if length < min_len:
                    min_len = length
                    start = left

                # Remove leftmost character
                window[s[left]] -= 1

                # Check if removing it makes window invalid
                if s[left] in need:
                    if window[s[left]] < need[s[left]]:
                        have -= 1

                left += 1

        # Step 5: Return the minimum substring
        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]