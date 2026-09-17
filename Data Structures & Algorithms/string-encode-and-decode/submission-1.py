class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            str_enc = str(l) + "-" + s
            res += str_enc
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        dele = "-"
        n = len(s)
        idx = 0
        while idx < n:
            ln = "0"
            while idx < n and s[idx] != dele:
                ln += s[idx]
                idx += 1
            ln = int(ln)
            idx += 1 # removing delimiter

            res.append(s[idx: idx+ln])
            idx += ln
        return res
