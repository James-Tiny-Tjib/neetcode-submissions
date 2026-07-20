class Solution:
    def trap(self, height: List[int]) -> int:
    
        l = 0
        r = len(height)-1

        max_L = height[l]
        max_R = height[r]
        
        result = 0
        while l < r:

            if max_L < max_R:
                l +=1
                max_L = max(max_L, height[l])
                result += max_L - height[l]
            else:
                r -=1
                max_R = max(max_R, height[r])
                result += max_R - height[r]
        
        return result
                
        
