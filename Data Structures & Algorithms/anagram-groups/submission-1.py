class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ctr = [0]*26
            for ch in s:
                ctr[ord(ch) - ord('a')] += 1
            res[tuple(ctr)].append(s)
        return list(res.values())
