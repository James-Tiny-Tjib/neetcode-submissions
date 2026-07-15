class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # num_counts = {}
        # for i in range(0, len(nums)):

        #     diff = target - nums[i]

        #     if num_counts.get(diff) is None:
        #         num_counts[nums[i]] = i
        #     else:
        #         return [num_counts[diff],i]

        num_counts = {}
        for i in range(0, len(nums)):

            if num_counts.get(target - nums[i]) is None:
                num_counts[nums[i]] = i
            else:
                return [num_counts[target - nums[i]],i]