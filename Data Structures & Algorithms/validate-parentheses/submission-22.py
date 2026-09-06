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
            
            # If an end bracket is found, we need to immediately delete its opening bracket so 
            # that we can do our checking method, which is whether stack is empty or not when we remove
            # pairs of parantheses in roder
            if c in par_pair:

                # Quick check: if stack was empty, there's no opening bracket. Return False 
                if len(stack) == 0:
                    return False
                # Now check if the last item in the list is its opening bracket. If so, remove immediately
                # The reason we can't do != and False is bc we need to check if the stack is not empty, and 
                # once that it is not empty, then check if its a pair
                if stack and stack[-1] == par_pair[c]:
                    stack.pop()
                else:
                    return False
                
            # This means its an opening pair. Add it to the stack
            else:
                stack.append(c)
            
        # Return True if the stack is empty
        return not stack
