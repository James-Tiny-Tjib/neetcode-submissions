class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1

        # Standard While Loop 
        while l <= r:

            # mid and match target if possible
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            
            # Branch A: Is fold within [mid, r]
            # This means that [mid, r] contains [mid, max] U [min, r]
            # [mid, r] is not sorted
            elif nums[r] < nums[mid]:
                # Remember: [mid, max] U [min, r]
                # In this case, we are checking if target falls within [mid, r]
                # Is the target bigger than mid and less than or equal to r
                # If thats the case, the target is within [mid, r] and we eliminate the left
                if target > nums[mid] or target <= nums[r]:
                    l = mid + 1

                # Otherwise get rid of all the right
                else:
                    r = mid - 1

            
            # Branch B: The Right is Sorted
            # Just check if its in the right at all, if it is, shrink the left
            # If not, shrink the right
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

                


# target 4
# 3 4 5 6 1 2