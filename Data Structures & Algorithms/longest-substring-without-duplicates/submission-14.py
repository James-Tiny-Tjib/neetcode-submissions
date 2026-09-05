class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # The Idea: Start making a hashset that contains all the values of the substring
        # Then, grow the window if the new item isn't in the hashset
        # Else move the left pointer and remove the item that was there up until the duplicate of s[r] is removed

        # Max length
        max_len = 0

        # Hashset to store the chars in the substring
        substr_hs = set()

        # left pointer
        l = 0

        # Move right pointer all the time
        for r in range(len(s)):

            # Ensure that before adding the s[r], its duplicate 
            # if applicable gets removed by shrinking the left
            while s[r] in substr_hs:
                substr_hs.discard(s[l])
                l += 1
            
            # Add the char to the set
            substr_hs.add(s[r])

            # Update the height
            max_len = max(max_len, len(substr_hs))

        # Return the max
        return max_len

        
