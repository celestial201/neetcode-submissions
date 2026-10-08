class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        if n == 0:
            return

        k = k % n

        # Step 1: Reverse the entire array
        left = 0
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Step 2: Reverse the first k elements
        left = 0
        right = k - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Step 3: Reverse the remaining elements
        left = k
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1