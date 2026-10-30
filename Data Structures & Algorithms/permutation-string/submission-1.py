class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer, permutation is impossible
        if len(s1) > len(s2):
            return False

        freq = {}
        window_freq = {}

        left = 0
        right = len(s1) - 1

        # Frequency of s1
        for char in s1:
            freq[char] = 1 + freq.get(char, 0)

        # Frequency of first window in s2
        for i in range(left, right + 1):
            window_freq[s2[i]] = 1 + window_freq.get(s2[i], 0)

        # Slide the window
        while right < len(s2):

            # Check current window
            if freq == window_freq:
                return True

            # Remove the left character
            window_freq[s2[left]] -= 1

            if window_freq[s2[left]] == 0:
                del window_freq[s2[left]]

            # Move the window
            left += 1
            right += 1

            # Add the new right character
            if right < len(s2):
                window_freq[s2[right]] = 1 + window_freq.get(s2[right], 0)

        return False