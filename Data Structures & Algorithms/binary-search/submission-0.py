class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        h = n - 1

        while l <= h:
            guess = (l + h) // 2

            if nums[guess] < target:
                l = guess + 1

            elif nums[guess] > target:
                h = guess - 1

            else:
                return guess

        return -1