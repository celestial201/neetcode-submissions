class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrams = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in angrams:
                angrams[key] = []
            angrams[key].append(word)
        return list(angrams.values())