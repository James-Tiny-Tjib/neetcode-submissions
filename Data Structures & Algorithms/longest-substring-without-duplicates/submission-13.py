class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # The Idea: Start making a hashset that contains all the values of the substring
        # Then, grow the window if the new item isn't in the hashset
        # Else move the left pointer and remove the item that was there up until the duplicate of that 

        # # If empty, return 0
        # if len(s) == 0: return 0

        # max_len = 1
        # substr_hs = set()
        # l = 0

        # # Put the first char into set
        # substr_hs.add(s[l])

        # for r in range(1,len(s)):

        #     if (s[r] in substr_hs):
        #         substr_hs.remove(s[l])
        #         l += 1
            
        #     substr_hs.add(s[r])

        #     max_len = max(max_len, len(substr_hs))

        # return max_len

        max_len = 0
        substr_hs = set()
        l = 0

        for r in range(len(s)):


            while s[r] in substr_hs:
                substr_hs.discard(s[l])
                l += 1
            
            substr_hs.add(s[r])

            max_len = max(max_len, len(substr_hs))

        return max_len

        
