class Solution:
    def minWindow(self, s: str, t: str) -> str:
         
        if t == "" or len(s) < len(t):
            return ""
        
        count_t = {}
        window = {}
        res_l = -1
        res_r = -1
        res_len = float('inf')
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        # Left Pointer
        l = 0

        # Have - keeps track of how many matches we have
        have = 0

        # Need - Compares to current situation to determine if have has enough
        need = len(count_t)
        

        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count_t and (window[s[r]] == count_t[s[r]]):
                have += 1
            
            while have == need:

                if (r - l + 1) < res_len:
                    res_l = l
                    res_r = r
                    res_len = (r - l + 1)

                if(window[s[l]] - 1 < count_t.get(s[l], 0)):
                    have -= 1
                
                window[s[l]] -= 1
                l +=1
            
        return s[res_l:res_r+1] if res_len != float("inf") else ""
            
            


            
            
            




        

        