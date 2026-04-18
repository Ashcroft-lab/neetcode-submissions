class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for st in strs:
            x = "".join(sorted(st))
            if x not in di:
                di[x] = []
            di[x].append(st)
        return di.values()
