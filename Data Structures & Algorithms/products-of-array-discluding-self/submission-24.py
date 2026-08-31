class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums = [1, 2, 4, 6]
        # ans = [48, 24, 12, 8]

        # Define
        # n = 4
        n = len(nums)

        # Keep track of the result
        # [0, 0, 0, 0]
        res = [0] * n

        # Prefix Product (value is the product of all the items before)
        # [0, 0, 0, 0]
        pref = [0] * n

        # Suffix Product (value is the product of all the items after)
        # [0, 0, 0, 0]
        suff = [0] * n

        # Set the default to be 1 at each respective end
        # [1, 0, 0, 0]
        pref[0] = 1

        # [0, 0, 0, 1]
        suff[-1] = 1


        # Populate Prefix Array
        # The goal is that the current index has all the numbers multiplied up to that point (exclusive)
        # Range is from [1, n) bc there's no i-1 @ i = 0
        # [1, 0, 0, 0] (Start)
        # [1, 1, 0, 0] 1 * 1 = 1
        # [1, 1, 2, 0] 1 * 2 = 2
        # [1, 1, 2, 8] 2 * 4 = 8
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i - 1]
            
        # Populate Suffix Array
        # The goal is that the current index has all the numbers multiplied up to that point (exclusive)
        # Range is from [n-2, -1) bc n-1 for index, and not i+1 @ i = n-1
        # [0, 0, 0, 1] (Start)
        # [0, 0, 6, 1] 1 * 6 = 6
        # [0, 24, 6, 1] 6 * 4 = 24
        # [48, 24, 6, 1] 24 * 2 = 48
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i + 1]

        # Populate The Result by multiplying the prefix and suffix together
        # [ 1,  1,  2,  8]
        #   *   *   *   *
        # [48, 24,  6,  1]
        #   =   =   =   =
        #  48  24  12   8
        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res       
        



