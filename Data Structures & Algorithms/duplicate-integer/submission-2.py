class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return False
        num_set = set()
        for n in nums:
            if not n in num_set:
                num_set.add(n)
            else:
                return True
        
        return False

        