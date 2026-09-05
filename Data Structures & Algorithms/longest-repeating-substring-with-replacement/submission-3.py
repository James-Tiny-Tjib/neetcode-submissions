class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Dictionary (Key: Char, Value: freq)
        count = {}

        # Highest frequency historically
        res = 0

        # Left Pointer
        l = 0

        # Max Frequency character of current substring
        maxf = 0

        # Right pointer moves right every time
        for r in range(len(s)):
            
            # First add it into the frequency list
            count[s[r]] = count.get(s[r], 0) + 1

            # We should then update maxf, and the only way it could be de-throned 
            # is if the current char became larger than the frequency
            # Updating this now will make sure the 
            maxf = max(maxf, count[s[r]])

            # Now we need to check if the replacement rule
            # The rule is the the number of non-duplicates has to be smaller or equal to k
            # (r - l + 1) is the current length
            # If we subtract maxf from the length, then we know the non-duplicates

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1


            
            # Finally update the res
            res = max(res, r - l + 1)
        
        # Return res
        return res






