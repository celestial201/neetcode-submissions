class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0
        for num in res:
            if num - 1 not in res:
                current = num
                length = 1
                while current + 1 in res:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest
       