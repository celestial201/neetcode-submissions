class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        val_win = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            window_len = r - l + 1
            max_freq = max(count.values())
            replacements = window_len - max_freq

            while replacements > k:
                count[s[l]] -= 1
                l += 1
                window_len = r - l + 1
                max_freq = max(count.values())
                replacements = window_len - max_freq

            val_win = max(val_win, r - l + 1)
            r += 1

        return val_win