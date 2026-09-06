
# Import Deque since we need adding the popping elements on both sides of the deque.
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Left Pointer
        l = 0

        # Monotonic Deque
        dq = deque()

        # Save the results for every maximum. There is a total of len(nums) - k + 1 results
        res = [0] * (len(nums) - k + 1)

        # Move the right pointer every time 
        for r in range(0, len(nums)):
            
            # - The goal is to remove any elements from the front that has fallen out the window
            # - You'd think that we'd need a while loop to make sure that each element that has 
            #   fallen out the window gets popped? But you know need to check ONCE. Here's why:
            # - So we that this dq's elements are indices, and they too are in increasing order
            # (bc we add in from the right)
            # our loop increments r one time
            # 
            if dq and dq[0] < (r-k+1):
                dq.popleft()
            
            # Do the monotonic stack method here:
            # Pop off all items from the top of the stack until its no longer the biggest
            while dq and (nums[dq[-1]] < nums[r]):
                dq.pop()
            
            # Then add it
            dq.append(r)

            # Make sure that once we have fully constructed a full window, 
            # only then we add in the results
            if r + 1 >= k:
                # This mapping from r -> res using r + 1 - k
                # Assign the result to the first element in the dq
                res[r+1-k] = nums[dq[0]]

            l += 1

        return res



