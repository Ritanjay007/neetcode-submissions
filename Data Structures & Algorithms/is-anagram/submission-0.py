class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1=sorted(s)
        t1=sorted(t)
        for i in range(0,len(t)):
            if s1[i] != t1[i]:
                return False
        return True
        