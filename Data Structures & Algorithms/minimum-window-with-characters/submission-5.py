class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Quick Check
        if len(t) > len(s):
            return ""

        t_dict = {}
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        shortest = float("inf")
        curr_dict = {}

        l = 0
        best_l = 0          # FIX: save the best left pointer
        best_r = 0

        for r in range(len(s)):

            if s[r] in t_dict:

                # FIX: window is satisfied when every count is >= required count
                if all(curr_dict.get(c, 0) >= t_dict[c] for c in t_dict):

                    # Add s[r]
                    curr_dict[s[r]] = curr_dict.get(s[r], 0) + 1

                    # Shrink until another shrink would make it invalid
                    while True:
                        if s[l] not in curr_dict:
                            l += 1

                        elif curr_dict[s[l]] > t_dict[s[l]]:
                            curr_dict[s[l]] -= 1
                            l += 1

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

                    # FIX: allow extra copies of required characters
                    if all(curr_dict.get(c, 0) >= t_dict[c] for c in t_dict):

                        while True:
                            if s[l] not in curr_dict:
                                l += 1

                            elif curr_dict[s[l]] > t_dict[s[l]]:
                                curr_dict[s[l]] -= 1
                                l += 1

                            else:
                                break

                        # FIX: only update if this window is shorter
                        if r - l + 1 < shortest:
                            best_l = l
                            best_r = r
                            shortest = r - l + 1

        if shortest != float("inf"):
            # FIX: use the saved best_l, not the final l
            return s[best_l:best_r + 1]

        return ""