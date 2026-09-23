class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele = {}
        for i, num in enumerate(nums):
            if num not in ele:
                ele[num] = 1
            else:
                ele[num] += 1
        sorted_ele = sorted(ele.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_ele[:k]]