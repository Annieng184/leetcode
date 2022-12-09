class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_item = sorted(s)
        t_item = sorted(t)
        s_item.append(0) #to make the length equal else we will get list index out of bounds (1 extra char in string2)
        for i in range(len(t_item)):
            if s_item[i] != t_item[i]: #if character at i not same for both the strings, we get our answer 
                return t_item[i]
