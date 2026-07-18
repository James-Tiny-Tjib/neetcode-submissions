class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        max_streak = 0
        for n in nums:
            if n-1 not in num_set:
                test_num = n
                streak = 0
                while test_num in num_set:
                    test_num += 1
                    streak += 1
                if streak >= max_streak:
                    max_streak = streak
        
        return max_streak
        
        