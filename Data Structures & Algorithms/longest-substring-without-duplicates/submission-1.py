class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        r = 0
        max_l = 0

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])

            curr_l = r - l + 1
            max_l = max(max_l, curr_l)

            r += 1

        return max_l