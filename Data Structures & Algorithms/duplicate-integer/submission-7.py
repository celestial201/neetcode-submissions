class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     res={}
     for num in nums:
      if num not in res:
        res[num]=num
      elif num in res:
        return True
     return False
          
            
    
        