class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in summ:
                return [summ[diff], i]
            summ[num] = i