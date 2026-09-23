class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums  
            
        mid = len(nums) // 2
        arr_l = nums[:mid]
        arr_r = nums[mid:]
        
        sort_l = self.sortArray(arr_l)
        sort_r = self.sortArray(arr_r)
        i = 0
        j = 0
        merged = []
        
        while i < len(sort_l) and j < len(sort_r):
            if sort_l[i] < sort_r[j]:
                merged.append(sort_l[i])
                i += 1
            else:
                merged.append(sort_r[j])
                j += 1
        merged.extend(sort_l[i:])
        merged.extend(sort_r[j:])
        
        return merged