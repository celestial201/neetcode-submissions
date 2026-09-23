class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       ele={}
       for num in nums:
        if num not in ele:
             ele[num]=1
        else:
            ele[num]+=1
        for num in ele:
            if ele[num] >len(nums)/2:
              return num