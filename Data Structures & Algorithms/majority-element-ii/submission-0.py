class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      res={}
      count=0
      for num in nums:
        if num not in res:
            res[num]=1
        elif num in res:
            res[num] +=1
      answer=[]
      for num, frequency in res.items():
        if frequency > len(nums)//3:
            answer.append(num)
      return answer