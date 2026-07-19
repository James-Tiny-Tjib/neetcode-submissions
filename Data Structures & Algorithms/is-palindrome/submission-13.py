class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Lower case
        s_lower = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if not s_lower[left].isalnum():
                left +=1
            elif not s_lower[right].isalnum():
                right -=1
            elif s_lower[left] != s_lower[right]:
                return False
            else:
                left +=1
                right -=1
        
        return True

    
        