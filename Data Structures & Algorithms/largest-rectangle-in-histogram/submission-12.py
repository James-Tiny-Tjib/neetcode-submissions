class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        l = len(heights)

        max_area = 0

        stack = []

        for i in range(l + 1):

            while stack and (i == l or heights[stack[-1]] >= heights[i]):

                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, width * height)
            
            stack.append(i)

        return max_area

        