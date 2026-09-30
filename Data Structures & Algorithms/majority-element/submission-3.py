class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = {}

        for num in nums:
            ele[num] = 1 + ele.get(num, 0)

            if ele[num] > len(nums) // 2:
                return num
        