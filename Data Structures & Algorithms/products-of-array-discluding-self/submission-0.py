class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = []
        lp = 1
        for num in nums:
            op.append(lp)
            lp = lp * num
        rp = 1
        for i in range(len(nums) - 1, -1, -1):
            op[i] = op[i] * rp
            rp = rp * nums[i]   
        return op