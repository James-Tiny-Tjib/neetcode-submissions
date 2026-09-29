class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Number of Hours [1, len(piles)]
        l = 1
        r = max(piles)
        # Save the Result
        res = r
        while l <r:

            # Get the middle # of hours
            k = (l + r)//2

            # Count the total number of hours this could take if koko can eat k bananas/hr
            total = 0
            for b in piles:
                total += -(b//-k)
            
            # If the total was too large (meaning Koko ate too slow), increase the rate
            if total > h:
                l = k + 1

            # Otherwise k is a valid hour, and then save it. Then update r = k to keep on checking if smaller k exist
            else:
                res = k
                r = k
        
        return res

        
        