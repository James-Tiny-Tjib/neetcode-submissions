class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Define
        n = len(nums)
        # Keep track of the result
        res = [0] * n

        # Prefix Product (value is the product of all the items before)
        pref = [0] * n

        # Suffix Product (value is the product of all the items after)
        suff = [0] * n

        # Set the default to be 1
        pref[0] = 1
        suff[-1] = 1

        # Populate Prefix Array
        # Range is from [1, n) bc there's no i-1 @ i = 0
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i - 1]

        # Populate Suffix Array
        # Range is from [n-2, -1) bc n-1 for index, and not i+1 @ i = n-1
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i + 1]

        # Populate The Result
        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res       
        



