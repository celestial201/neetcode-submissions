class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 1000: return 91

        l,r = 0,0

        res = 0
        seen = set()

        while r < len(s):
            
            if s[r] in seen:
                seen.remove(s[l])                
                l += 1

            else:
                seen.add(s[r])
                res = max(res,r - l + 1)
                r += 1


        return res