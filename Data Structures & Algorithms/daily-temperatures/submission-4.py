class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Results. Initialize to 0 since they aren't guranteed to have a warmer day and wants those to be 0
        res = [0] * len(temperatures)
        
        # - Monotonically decreasing stack
        # - When the number gets popped off, we know that the temperature is larger there
        # - Then we can do some math with the indices to determine how many days it will take
        # - The key thing about monotonic stacks is that we insert them by order, so we can just
        #   store the indices as a 2 in 1.
        stack = []

        # Iterate through all the temperatures 
        for i, temp in enumerate(temperatures):

            # First check if the stack is empty, if so, then stop trying to remove
            # And check if the temperature last added was beaten by a higher temperature
            # If so, the one that is popped off how can do the calc to determine the number of days
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                res[index] = i - index
            
            # Once everything has been popped off, we can safely append a new value
            stack.append(i)
        
        return res


