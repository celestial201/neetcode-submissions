class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen:
                diff = abs(i - last_seen[num])

                if diff <= k:
                    return True

            last_seen[num] = i

        return False