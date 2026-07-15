class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest_streak = 0

        for n in nums:
            if not(n-1 in nums_set):
                current_num = n
                current_streak = 1

                while True:
                    if (n + current_streak) in nums_set:
                        current_streak += 1
                    else:
                        break
            
                if current_streak > longest_streak:
                    longest_streak = current_streak
        

        
        return longest_streak
        
            