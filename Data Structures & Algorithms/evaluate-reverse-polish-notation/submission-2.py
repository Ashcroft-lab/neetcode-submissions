class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for t in tokens:
            if t not in ("+", "-", "*", "/"):
                res.append(int(t))
            else:
                t1 = res.pop()
                t2 = res.pop()
                if t == "+":
                    res.append(t1+t2)
                elif t == "-":
                    res.append(t2-t1)
                elif t == "*":
                    res.append(t1*t2)
                elif t == "/":
                    res.append(int(float(t2)/t1))
        return res[0]
