class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_ct_1 = {}
        char_ct_2 = {}

        for c in s:
            if char_ct_1.get(c) is None:
                char_ct_1[c] = 1
            else:
                char_ct_1[c] += 1

        for c in t:
            if char_ct_2.get(c) is None:
                char_ct_2[c] = 1
            else:
                char_ct_2[c] += 1
        
        return char_ct_1 == char_ct_2
            

