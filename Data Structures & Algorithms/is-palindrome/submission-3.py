class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        s = "".join(char for char in s if char.isalnum())
        for i in range (0, len(s)):
            if (s[i] != s[len(s)-i-1]):
                return False
        
        return True