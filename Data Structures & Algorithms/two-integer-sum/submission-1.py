class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevhash= {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevhash:
                return [prevhash[diff], i]
            prevhash[n]=i