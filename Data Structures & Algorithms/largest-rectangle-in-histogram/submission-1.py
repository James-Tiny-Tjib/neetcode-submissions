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
                # If stack is not empty
                if stack:
                    width = i - stack[-1] - 1
                else:
                    # If stack is empty:
                    width = i

                # if height <= heights[i]:
                #     width += 1
                
                # print(height * width)
                if height * width > max_area:
                    max_area = height * width
            
            stack.append(i)
        
        return max_area


        