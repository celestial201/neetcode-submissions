class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        val_win = 0

        while r < len(s):
            # Add current character to the window
            count[s[r]] = count.get(s[r], 0) + 1

            # Calculate current window information
            window_len = r - l + 1
            max_freq = max(count.values())
            replacements = window_len - max_freq

            # Shrink window if too many replacements are needed
            while replacements > k:
                count[s[l]] -= 1
                l += 1

                # Recalculate after shrinking
                window_len = r - l + 1
                max_freq = max(count.values())
                replacements = window_len - max_freq

            # Current window is valid
            val_win = max(val_win, r - l + 1)

            # Expand window
            r += 1

        return val_win