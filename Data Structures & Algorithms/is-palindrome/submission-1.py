class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS= " ".join([c for c in s if c.isalnum()])
        newS=newS.lower()
        return newS==newS[::-1]
        
         

        