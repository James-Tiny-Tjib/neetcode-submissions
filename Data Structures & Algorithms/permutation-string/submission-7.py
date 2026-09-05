class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Small Edge Case
        if len(s1) > len(s2):
            return False
        
        # Initialize count arrays
        s1Count, s2Count = [0] * 26, [0] * 26

        # Initialize s1 freq arr, and the first sliding window of s2 freq arr
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count the number of matches
        matches = 0

        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Left Pointer
        l = 0
        for r in range(len(s1), len(s2)):
            # If matches == 26, always return true
            if matches == 26:
                return True
            
            # Dealing with matches by adding the char r from the right:
            # Update the window by adding the next char
            index = ord(s2[r]) - ord('a')
            s2Count[index] +=1
            # If adding it resulted it to be equal add one
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Else if adding made it one too much, we got to decrease matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Dealing with matches by removing the fchar l from the left
            # Update the window by removing the last char
            index = ord(s2[l]) - ord('a')
            s2Count[index] -=1
            # If adding it resulted it to be equal add one
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Else if deleting made it one too little, we got to decrease matches
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            l +=1
        
        return matches == 26





        
        

        

        