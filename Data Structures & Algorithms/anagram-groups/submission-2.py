class Solution:
    def get_key(self, word):
        arr = [""]*26
        for ch in word:
            arr[ord(ch) - ord("a")] += "."
        return "-".join(arr)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for word in strs:
            
            key = self.get_key(word)
            di[key] = di.get(key, [])
            di[key].append(word)
        return list(di.values())