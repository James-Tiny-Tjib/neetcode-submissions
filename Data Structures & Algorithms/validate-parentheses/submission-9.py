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

        for i in range(len(s)):
            
            if s[i] =="(" or s[i] =="{" or s[i] =="[":
                stack.append(s[i])
            
            if s[i] ==")" or s[i] =="}" or s[i] =="]":
                if stack and par_pair[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


        