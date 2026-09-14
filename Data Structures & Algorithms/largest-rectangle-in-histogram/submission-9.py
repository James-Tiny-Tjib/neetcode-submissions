class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Add 0 @ the end so that it can pop & do the final calculation
        heights.append(0)
        
        # Increasing Monotonic Stack [1, 2, 3 ...]
        stack = []

        # Store the current max area
        max_area = 0
        
        # Go Through the entire array
        for i in range(len(heights)):
            
            # If Stack is available and the current height is smaller than the       stack's last height (largest)
            while (stack and heights[stack[-1]] > heights[i]):

                # Pop the last index
                height_index = stack.pop()

                # Take the last index's height
                height = heights[height_index]

                # Calculate the Width
                
                # Case 1: The stack is not empty
                if stack:
                    # R - L - 1, don't include the walls
                    width = i - stack[-1] - 1

                # Case 2: The Stack is empty
                else:
                    # Set it to i, meaning no bar was shorter than the popped bar
                    # e.g [1,1]
                    width = i
                
                # Update the max_area
                if height * width > max_area:
                    max_area = height * width
            
            # Add the next index onto the stack
            stack.append(i)
        
        # Return max area
        return max_area


        