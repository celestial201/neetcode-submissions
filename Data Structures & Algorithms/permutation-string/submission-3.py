class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq={}
        s2_freq={}
        l=0
        r= len(s1)-1

        for char in s1:
            s1_freq[char]= 1 + s1_freq.get(char,0)
        for i in range(l, r+1):
            s2_freq[s2[i]]= 1+ s2_freq.get(s2[i],0)
        while r < len(s2):
            if s1_freq==s2_freq:
                return True
            s2_freq[s2[l]] -=1
            if s2_freq[s2[l]]==0:
                del s2_freq[s2[l]]
            l+=1
            r+=1
            if r < len(s2):
                s2_freq[s2[r]]= 1 + s2_freq.get(s2[r],0)
        return False

       