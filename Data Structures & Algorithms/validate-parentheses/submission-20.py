class Solution:
    def isValid(self, s: str) -> bool:
        
        # if the str is uneven, return False
        if len(s) == 1:
            return False

        # Define Stack
        stack = []
        
        # pair for parentheses
        par_pair = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        # Iterate Through each paranthese
        for c in s:
            
            if c in par_pair:
                if len(stack) == 0:
                    return False
                if stack and stack[-1] == par_pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        
        return not stack
