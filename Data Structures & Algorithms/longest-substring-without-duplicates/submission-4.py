class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        max_length = 0
        char_set = set()
        for r in range(len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
            else:
                while s[r] in char_set:
                    char_set.discard(s[l])
                    l +=1
                char_set.add(s[r])
            max_length = max(max_length, len(char_set))
        
        return max_length
