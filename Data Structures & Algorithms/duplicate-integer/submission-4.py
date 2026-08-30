class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if (len(nums) <= 1):
            return False

        hs = set()

        for n in nums:

            if n in hs:
                return True
            else:
                hs.add(n)

        return False 
        