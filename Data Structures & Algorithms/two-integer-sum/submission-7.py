class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_index_ht = {}

        for i, n in enumerate(nums):

            if (target - n) in num_index_ht:
                return [num_index_ht[target - n], i]
            else:
                num_index_ht[n] = i
        