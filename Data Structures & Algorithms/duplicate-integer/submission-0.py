class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dt = {}

        for n in nums:

            if dt.get(n) is None:
                dt[n] = n
            else:
                return True
            
        return False

        