from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = tuple(Counter(sorted(s)))
            if key not in d:
                d[key] = []
            d[key].append(s)
        return list(d.values())

        """
        dicts = []
        for s in strs:
            dicts.append(Counter(s))
        res = []
        sets = {}
        count = 0
        i = 0
        for dic in dicts:
            tup = tuple(sorted(dic.items()))
            if tup in sets.keys():
                idx = sets.get(tup)
                res[idx].append(strs[i])
            else:
                sets[tup] = count
                count += 1
                res.append([strs[i]])
            i += 1
        return res
    """
"""
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = tuple(sorted(Counter(s).items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
"""