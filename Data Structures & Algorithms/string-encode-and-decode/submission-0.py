class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str=""
        for words in strs:
            E= str(len(words)) + "#" + words
            encode_str += E
        return encode_str

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
           j= s.find("#", i)
           length=int(s[i:j])
           word = s[j + 1 : j + 1 + length]
           res.append(word)
           i = j + 1 + length
        return res

