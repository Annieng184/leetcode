class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_item = sorted(s)
        t_item = sorted(t)
        s_item.append(0)
        for i in range(len(t_item)):
            if s_item[i] != t_item[i]:
                return t_item[i]
