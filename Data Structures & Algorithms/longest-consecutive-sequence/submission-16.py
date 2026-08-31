class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        m = 0
    
        # Convert to set
        n_set = set(nums)

        for n in nums:
            if not (n-1) in n_set:
                curr = 0
                while (n + curr) in n_set:
                    curr += 1
                m = max(curr, m)
                
        
        return m
        
