class Solution:
    def findMin(self, nums: List[int]) -> int:

        # if nums[0] <= nums[-1]:
        #     return nums[0]
        
        l = 0
        r = len(nums) - 1
        while l < r:

            mid = (l + r)//2

            # This one also had the l<=r && r = mid - 1 pattern
            # In this case, we needed to check if we hit the target, and then do the others
            # Safe and explicit, but bad since we need so many checks
            # Since this is a search question, not an optimize, we should use the other pattern instead
            # This way we can skip the conditional to check if its the target, adn return it at the end.

            # if nums[mid - 1] > nums[mid]:
            #     return nums[mid] 
            # elif nums[mid] > nums[r]: 
            #     l = mid + 1
            # else:
            #     r = mid - 1

            if nums[mid] > nums[r]: 
                l = mid + 1
            else:
                r = mid
        
        return nums[r]