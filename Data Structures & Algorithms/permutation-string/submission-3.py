class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_freq_list = [0] * 26
        s2_freq_list = [0] * 26
    
        # Create first freq list for s1 and s2
        for i in range(len(s1)):
            s1_freq_list[ord(s1[i])-ord('a')] += 1
            s2_freq_list[ord(s2[i])-ord('a')] += 1

        # Do the checking thing
        for i in range(len(s1),len(s2)):
            if s2_freq_list == s1_freq_list:
                return True
            s2_freq_list[ord(s2[i-len(s1)]) - ord('a')] -= 1
            s2_freq_list[ord(s2[i]) - ord('a')] += 1
        
        # Do the final check that the for loop
        return s2_freq_list == s1_freq_list
            
            
            
            

            

        
        
