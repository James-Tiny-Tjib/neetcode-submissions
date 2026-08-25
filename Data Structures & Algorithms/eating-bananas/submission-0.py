class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # If there are n piles, the fastest Koko can eat the bananas is n hours since she can only eat at most 1 pile an hour

        # Brute Force Method would be to try k = 1, k = 2, etc...
        # The worst case k would be the biggest pile (hence the time complexity n * log(m)), m
        # This means trying k is going to be binary search
        # And instead of doing, 1, 2, 3, ..., we can get the lower (1) and upper bound (m), and do binary search on that.

        # Now how do we do that?
        # We can iterate each pile for a given k, and check if we were in or out of budget of h hours
        # If we were in, we shutdown the upper bound, else the lower.
        # But we need to make sure that the stopping condition works

        l = 1
        r = max(piles)
        res = r
        while l <= r:

            mid =(l + r) // 2
            
            # Calculate the number of hours required 
            hours = 0
            for p in piles:
                # Floor division
                hours += - (p // -mid)

            if hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

            
            

                

