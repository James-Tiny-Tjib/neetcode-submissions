class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Trivial Solution
        # If its in order, return the first element
        # Its only in order when the last number is larger than the first
        if  nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2
            
            if (nums[mid] > nums[r]):
                l = mid + 1 
            else:
                r = mid 
        
        return nums[l]
        
        
        

        
        


        
        