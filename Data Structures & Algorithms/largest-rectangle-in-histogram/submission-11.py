class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        l = len(heights)
        
        # Storing the Max Area
        max_area = 0

        #  - Strictly Increasing Monotonic Stack
        #  - This will keep track of the left border, where if we pop off the current
        #    element and do its calculation, the left boundary's index is the next   
        #    element on the stack
        #  - The reason that it is a strictly increasing monotonic stack is bc if 
        #    there were 2 element of the same height, we can just get rid of the 
        #    earlier one since it contains no useful infomation as the width is the 
        #    same for both calculations (we'd actually need to iterate twice and an 
        #    unnecssary one too)
        #  - E.g. if there was heights = [2,4,4,1], 
        #    In the increasing case @ i=2: [0,1,2]
        #    In strictly increasing case @ i=2 [0,2]. 
        #    Notice that increasing would require a 4 * 1 calculation after the 4 * 2
        #    And if we omitted it, the width calculation still exists
        stack = []

        # - This implementation has a very similar idea to Brute Force: 
        #   Locate the left and right boundaries keeping the height h.
        # - The idea is once we find the left and right boundaries, we know
        #   the width, and we can multiply it by the height to get, and compare
        #   that to the max Area

        # - Our loop goes from [0, n + 1), so technically [0,n]. Why?
        # - The reason is because we only do the max calculation when there is a pop
        #   and we never calculate heights if there was no popping. This applies 
        #   heights where there was no smaller height after
        #   What we'll do is that we'll continuously pop once we reach the end of the 
        #   list, and pretend there is a 0 at the end
        for i in range(l + 1):

            #  - This is the monotonic strictly increasing stack   
            #  - First, while stack ensures the list isn't empty
            #  - We are also familar with the monotonic rule (Strictly too, though 
            #    tehcnically won't break anything)
            #  - The only special thing is the i == l, which handles the special case 
            #    when we reach the end where we have to pop everything and get those heights
            while stack and (i == l or heights[stack[-1]] > heights[i]):
                
                # We pop off the height
                height = heights[stack.pop()]

                # - We need to calculate the width next.
                # - We need to get the left and right boundaries non-inclusive
                # - This means (right-1) - (left+1) - 1 -> right - left - 1
                # - Here's the kicker: if popping this bar makes the stack empty,
                #   then there is no shorter bar to its left.
                #   Therefore, its rectangle can extend all the way back to index 0,
                #   so the width is i.
                width = i if not stack else i - stack[-1] - 1

                # Now we can calculate the area and update the max
                max_area = max(height*width, max_area)
            
            # Once we did all that we can monotonically add the next item
            stack.append(i)
        
        return max_area



        