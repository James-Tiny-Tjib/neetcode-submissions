class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_ht = {}
        t_ht = {}

        for c in s:
            s_ht[c] = s_ht.get(c,0) + 1

        for c in t:
            t_ht[c] = t_ht.get(c,0) + 1
        
        return s_ht == t_ht

        