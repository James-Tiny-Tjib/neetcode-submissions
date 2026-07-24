from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Store Results Here (only nums - k + 1 results)
        res = [-1] * (len(nums) - k + 1)

        # Define Deque
        dq = deque()
        
        # Iterate through the entire array
        for r in range (len(nums)):
            
            # If the largest number is out of the window, remove it from the deque
            if dq and dq[0] < ( r - k + 1):
                dq.popleft()

            # Update the Deque
            while (dq and nums[r] > nums[dq[-1]]):
                dq.pop()

            # Add the next element to the deque
            dq.append(r)

            # Then only add teh results if a window is fully constructed 
            if (r - k + 1) >= 0:
                res[r-k + 1] = nums[dq[0]]  

        return res   

