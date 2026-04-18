class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # create a max stack idx
        max_idx = []
        res = [0]*len(temp)
        for i in range(len(temp)-1, -1, -1):
            if not max_idx:
                max_idx.append(i)
            while max_idx and temp[i] >= temp[max_idx[-1]]:
                max_idx.pop()

            res[i] = max_idx[-1] -i if max_idx else 0
            max_idx.append(i)
        return res