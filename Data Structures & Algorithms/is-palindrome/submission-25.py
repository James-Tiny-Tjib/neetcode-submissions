class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        while l < r:

            while (not self.is_alnum(s[l])) and l < r:
                l += 1
            
            while not self.is_alnum(s[r]) and l < r:
                r -= 1;
            
            if (s[l].lower() == s[r].lower()):
                l += 1
                r -= 1
            else:
                return False
        
        return True

    



    def is_alnum(self,c):
        return (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c)  <= ord('9')
        )