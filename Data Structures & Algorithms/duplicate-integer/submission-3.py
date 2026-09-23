class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      ele={}
      for num in nums:
        if num not in ele:
            ele[num]=1
        else:
            ele[num] +=1
        if ele[num] > 1:
            return True
      return False
        
          
            
    
        