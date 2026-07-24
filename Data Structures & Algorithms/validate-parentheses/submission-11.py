class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        # Define Stack
        stack = []
        
        # pair for parentheses
        par_pair = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        for c in s:

            if c in par_pair:
                if stack and par_pair[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack


        