class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Left and Right pointers
        l = 0
        r = len(nums) - 1
        
        # Keep iterating until l > r
        while l <= r:

            # Calculate mid
            mid = (l + r) // 2

            # If mid is the target, return
            if nums[mid] == target:
                return mid
            # Else if the target is larger, set l to mid + 1
            elif target > nums[mid]:
                l = mid + 1
            # Else if the targer is smaller, set r to mid - 1
            else:
                r = mid - 1
        
        # Return -1 if the target is not found
        return -1


        