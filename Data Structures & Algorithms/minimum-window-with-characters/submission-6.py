class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Quick Check
        if (len(t) > len(s)):
            return ""

        t_dict = {}                 # Keep the frequncies of require characters
        for c in t:                 # Create a list of all the frequencies
            t_dict[c] = t_dict.get(c, 0) + 1
        shortest = 1001             # Define the shortest length 
        curr_dict = {}              # Define current dict with all required chars
        l = 0                       # left pointer
        best_l = 0          # FIX: save the best left pointer
        best_r = 0                  # Best r pointer


        # For loop to iterate r
        for r in range(len(s)):
            
            # Wrap this cond. so actions only occur when relevant chars are reached
            if s[r] in t_dict:

                # Case 1: If already satisfied, and want to check if shrinking can occur
                if all(curr_dict.get(c, 0) >= t_dict[c] for c in t_dict):

                    # Add s[r] back in
                    curr_dict[s[r]] = curr_dict.get(s[r], 0) + 1

                    # Loop and Shrink until you reach a letter that can't be shrunk
                    while True:
                        # Move l by 1 if s[l] isn't in curr_dict
                        if not s[l] in curr_dict:
                            l += 1
                        # Else we can subtract s[l] and still be fine
                        elif curr_dict[s[l]] > t_dict[s[l]]:
                            curr_dict[s[l]] -= 1
                            l +=1
                        # Else break-
                        else:
                            break

                    # FIX: only update if this window is shorter
                    if r - l + 1 < shortest:
                        best_l = l
                        best_r = r
                        shortest = r - l + 1
                else:
                    # Add s[r]
                    curr_dict[s[r]] = curr_dict.get(s[r], 0) + 1

                    if all(curr_dict.get(c, 0) >= t_dict[c] for c in t_dict):
                        # Loop and Shrink until you reach a letter that can't be shrunk
                        while True:
                            # Move l by 1 if s[l] isn't in curr_dict
                            if not s[l] in curr_dict:
                                l += 1
                            # Else we can subtract s[l] and still be fine
                            elif curr_dict[s[l]] > t_dict[s[l]]:
                                curr_dict[s[l]] -= 1
                                l +=1
                            # Else break
                            else:
                                break

                        # FIX: only update if this window is shorter
                        if r - l + 1 < shortest:
                            best_l = l
                            best_r = r
                            shortest = r - l + 1



        # Final Return
        if shortest != 1001:
            # Return String
            return s[best_l:best_r+1]
        else:
            return ""


            


        