class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Results
        res = [0] * len(temperatures)
        
        # Monotonically Increasing stack
        # When the number gets popped off, we know that the temperature is larger there
        # Then we can do some math with the indices to determine how many days it will take
        # The key thing about monotonic stacks is that we insert them by order, so we can just
        # store the indices as a 2 in 1.
        stack = []

        # Iterate through the 
        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                res[index] = i - index
            
            stack.append(i)
        
        return res


