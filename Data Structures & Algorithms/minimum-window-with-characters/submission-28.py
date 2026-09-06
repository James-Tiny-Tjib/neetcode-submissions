class Solution:
    def minWindow(self, s: str, t: str) -> str:


        # Edge case 
        if t == "" or len(s) < len(t):
            return ""
        
        # Hash table for t
        count_t = {}
        # Adding to the Hash table
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        # Hash table for window
        window = {}

        # Saving the Result's information
        res_l = -1
        res_r = -1
        res_len = float('inf')

        # Left Pointer
        l = 0

        # Have - keeps track of how many character's character frequency match with t
        # e.g if need has 2 a's and the window also has them, have +=1, not 2
        have = 0

        # Need - Compares to current situation to determine if have has enough
        # This mechanism of have and need allows us to keep track of whether the substring 
        # contains t without having to compare the frequency of each. We don't need to do that.
        # All we need to keep track of are these conditions, and the things that we will need to modify
        # and access when we move or shrink the window is accessible via the pointers. 
        need = len(count_t)
        
        # Iterate r
        for r in range(len(s)):
            
            # Add r to the window
            window[s[r]] = window.get(s[r], 0) + 1

            # If adding r satisfies the count_t freq, have += 1
            if s[r] in count_t and (window[s[r]] == count_t[s[r]]):
                have += 1
            
            # We want the shrink the substring as much as possible without violating the have == needd
            # This acts as a while loop conditional + an if statement for whether they were equal 
            # and can enter the while loop
            while have == need:
                
                # If we found a smaller substring, save it
                if (r - l + 1) < res_len:
                    res_l = l
                    res_r = r
                    res_len = (r - l + 1)

                # If shrinking the window hurts the "have" contract, update have
                if(window[s[l]] - 1 < count_t.get(s[l], 0)):
                    have -= 1
                
                # Shrink / move the window forward regardless of the statement above
                # We have a solution saved already
                window[s[l]] -= 1
                l +=1
        
        # Return the substring if found. If res_len hasn't been set, no sol. was found and return ""
        return s[res_l:res_r+1] if res_len != float("inf") else ""
            
            


            
            
            




        

        