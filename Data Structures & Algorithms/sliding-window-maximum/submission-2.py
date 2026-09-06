
# Import Deque since we need adding the popping elements on both sides of the deque.
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Left Pointer
        l = 0

        # Monotonic Deque
        dq = deque()

        # Save the results for every maximum
        res = [0] * (len(nums) - k + 1)

        # Move the right pointer every time 
        for r in range(0, len(nums)):

            if dq and dq[0] < (r-k+1):
                dq.popleft()

            while dq and (nums[dq[-1]] < nums[r]):
                dq.pop()
            
            dq.append(r)

            if r + 1 >= k:
                res[r+1-k] = nums[dq[0]]

            l += 1

        return res



