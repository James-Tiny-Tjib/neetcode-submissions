class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        # 2 Central Ideas:
        # - In order to find the water trapped within an index, we can use the formula:
        #   min(max height left of the index, max heigh right of the index) - height of current index
        #   min(maxL, maxR) - height[i], and if its negative, ignore it. 
        # - The next idea is that we need to keep track of left and right pointers as well as the left
        #   and right heights. We always move the smallest pointer so we know that whenever it lands on  
        #   another height, the minimum is retrieved. This is important since all we need to know is the
        #   MINIMUM of the max_L and max_R pointers
        # - Other key details: 
        #   * Only update the maxL and maxR after the water calculation
        
        # Set l & r
        l = 0
        r = len(height) - 1

        # Set maxL and maxR to the height of the left and right pointers
        maxL = height[l]
        maxR = height[r]

        # Total Water
        res = 0

        # Start with double pointer while loop
        while l < r:

            # Move the smaller pointer towards the middle
            if maxL < maxR:
                l +=1
                res += max(0, min(maxL, maxR) - height[l])
                maxL = max(height[l], maxL)
            else:
                r -=1
                res += max(0, min(maxL, maxR) - height[r])
                maxR = max(height[r], maxR)               

        return res
            





        
        