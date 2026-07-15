class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Master Dictionary:
        # Keys: Dictionaries where:
            # Keys: char
            # Values: number of times it appears
        # Values: List of Strings

        master_dict = {}

        for s in strs:
            str_dict = {}
            for c in s:
                if str_dict.get(c) is None:
                    str_dict[c] = 1
                else:
                    str_dict[c] += 1
            
            str_dict = frozenset(str_dict.items())

            if master_dict.get(str_dict) is None:
                master_dict[str_dict] = [s]
            else:
                master_dict[str_dict].append(s)
        
        return list(master_dict.values())
            

                
        