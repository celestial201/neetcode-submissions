class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):  # Hardcoded to 2 instead of x
            for n in nums:
                ans.append(n)
        return ans