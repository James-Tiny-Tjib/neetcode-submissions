class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Trivial Solution
        # If its in order, return the first element
        # Its only in order when the last number is larger than the first
        if  nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        
        # Set the left and right pointer
        l = 0
        r = len(nums) - 1

        # While l < r. Does not do l == r bc then l would be the minimum value
        while l < r:
            
            # Calculate Minimum
            mid = (l + r) // 2
            
            # If the mid > r, that means everything from l to mid is sorted 
            # and none of those can be the numbers at the boundary
            # Additionally, mid can't be the smallest since its at least larger than r
            if (nums[mid] > nums[r]):
                l = mid + 1 
            
            # Otherwise, the boundary can't be above the mid but still be the mid itself
            else:
                r = mid 
        
        # Return the left number 
        return nums[l]
        
        
        

        
        


        
        