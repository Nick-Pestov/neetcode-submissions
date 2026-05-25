from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            if key not in d:
                d[key] = []
            d[key].append(s)
        return list(d.values())
