class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_dict = defaultdict(list)
        
        for s in strs:

            c_freq = [0] * 26

            for c in s:
                c_freq[ord(c) - ord('a')] +=1
            
            c_freq = tuple(c_freq)

            result_dict[c_freq].append(s)

        
        return list(result_dict.values())
            

            
            
            

