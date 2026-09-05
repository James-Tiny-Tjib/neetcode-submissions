class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "" or len(s) < len(t):
            return ""

        # Vars
        count_t, window = {}, {}
        l = 0
        res_l, res_r = -1,-1
        res_len = float('inf')

        # Populate count_t
        for c in t:
            count_t[c] = count_t.get(c,0) + 1

        # need = len(count_t) bc need should be the number of unique chars
        have, need = 0, len(count_t)


        # Have r iterate through all chars in s
        for r in range(len(s)):
            
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in count_t and (window[c] == count_t[c]):
                have += 1

            while have == need:
                
                if (r - l + 1) < res_len:
                    res_l = l
                    res_r = r
                    res_len = (r - l + 1)
                
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        return s[res_l: res_r + 1]  if res_len != float('inf') else ""





        