class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        # 2 Central Ideas:
        # - In order to find the water trapped within an index, we can use the formula:
        #   min(max height left of the index, max heigh right of the index) - height of current index
        #   min(maxL, maxR) - height[i], and if its negative, ignore it. 
        # - The next idea is that we need to keep track of left and right pointers as well as the left
        #   and right heights. We always move the smallest pointer so we know that whenever it lands on  
        #   another height, the minimum is retrieved. This is important since all we need to know is the
        #   MINIMUM of the max_L and max_R pointers. The one that is moved the is the minimym bottleneck
        #   since it was the smaller one
        # - Other key details: 
        #   * The order of updating maxL and result matters, but both ways can be done
        #     * If you update the result before updating maxL (described in the video, not the one coded),
        #       you'd need to check if the result is negative, and make sure that if it is, it's 0.
        #     * If you update the result after the maxL, it may seem like it might not work because the
        #       current height could be bigger than the maxL or maxR, and the height itself isn't the wall's 
        #       actual height, but it actually works out because if height[l] >= maxL, then 
        #       height[l] - height[l] = 0, and you don't need make sure what's being added is positive
        
        # Set l & r
        l = 0
        r = len(height) - 1

        # Set maxL and maxR to the height of the left and right pointers 
        # because thats the height so far (you'd also won't know which to move intitally)
        maxL = height[l]
        maxR = height[r]

        # Total Water
        res = 0

        # Start with double pointer while loop
        while l < r:
            # Version 1
            # # Move the smaller pointer towards the middle
            # if maxL < maxR:
            #     l +=1
            #     res += max(0, maxL - height[l])
            #     maxL = max(height[l], maxL)
            # else:
            #     r -=1
            #     res += max(0, maxR - height[r])
            #     maxR = max(height[r], maxR) 

            # Version 2
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                res += maxR - height[r]



        return res
            





        
        