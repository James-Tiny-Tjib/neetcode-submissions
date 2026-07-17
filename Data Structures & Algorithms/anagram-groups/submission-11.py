class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        combo_dict = defaultdict(list)

        for s in strs:

            s_char_list = [0] * 26

            for c in s:

                s_char_list[ord(c) - ord('a')] += 1

            s_char_tp = tuple(s_char_list)
            
            combo_dict[s_char_tp].append(s)
    
        return list(combo_dict.values())




