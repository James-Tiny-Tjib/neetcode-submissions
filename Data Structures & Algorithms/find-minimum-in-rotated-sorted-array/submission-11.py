class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Trivial Solution
        # If its in order, return the first element
        # Its only in order when the last number is larger than the first
        if  nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            # Test if its the boundary:
            if (mid != 0) and (nums[mid] - nums[mid - 1] < 1):
                return nums[mid]
            elif (l != 0) and (nums[l] - nums[l - 1] < 1):
                return nums[l]
            elif (r != 0) and (nums[r] - nums[r - 1] < 1):
                return nums[r]
            
            if (nums[mid] < nums[l]):
                r = mid - 1
            else:
                l = mid + 1 
        
        
        

        
        


        
        