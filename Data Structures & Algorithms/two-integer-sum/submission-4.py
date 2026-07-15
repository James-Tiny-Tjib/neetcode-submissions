class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dict = {}

        for i, n in enumerate(nums):
            if not target - n in num_dict:
                num_dict[n] = i
            else:
                return [num_dict[target-n],i]
        