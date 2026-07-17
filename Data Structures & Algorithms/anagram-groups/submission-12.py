class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Key: (0 * 26), where each index represents a letter, and the number = frequency of the letter 
        # Value: the list of Strings that are anagrams
        # Default dict to ensure the default value is an empty list
        combo_dict = defaultdict(list)

        # Iterate Through Each String
        for s in strs:

            # Init arr
            s_char_list = [0] * 26

            # Populate frequency char list
            for c in s:

                s_char_list[ord(c) - ord('a')] += 1

            # Make tuple (immutable)
            s_char_tp = tuple(s_char_list)
            
            # Add to 
            combo_dict[s_char_tp].append(s)

        # Return just the values casted as a list
        return list(combo_dict.values())




