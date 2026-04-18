class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False

        par_map = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        stack = []
        for par in s:
            if par in par_map:
                stack.append(par_map[par])
            elif stack and par == stack.pop():
                pass
            else:
                return False
        if stack:
            return False
        return True