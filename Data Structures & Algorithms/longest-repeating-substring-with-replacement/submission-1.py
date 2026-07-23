class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        l = 0 # Left part of the window
        max_streak = 0
        char_dict = {}
        max_F = 0

        for r in range(len(s)):

            # Add current char into dictionary
            char_dict[s[r]] = char_dict.get(s[r],0) + 1

            # Update max_F (either keep it max_F or whatever changed by adding s[r])
            max_F = max(max_F, char_dict[s[r]])

            if (r - l+1) - max_F > k:
                # If the max_F came from the s[l] char, subtract it
                if max_F == char_dict[s[l]]:
                    max_F -= 1
                # Subtract that frequency
                char_dict[s[l]] -= 1
                l += 1

            max_streak = max(max_streak, r-l+1)
                

        return max_streak