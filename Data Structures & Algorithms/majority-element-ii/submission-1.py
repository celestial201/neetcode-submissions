class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = {}

        for num in nums:
            res[num] = res.get(num, 0) + 1

        answer = []

        for num, frequency in res.items():
            if frequency > len(nums) // 3:
                answer.append(num)

        return answer