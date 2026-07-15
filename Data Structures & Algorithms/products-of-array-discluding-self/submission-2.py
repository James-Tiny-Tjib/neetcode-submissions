class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref_sum = [1] * len(nums)
        suff_sum = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            pref_sum[i]  = pref_sum[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suff_sum[i] = suff_sum[i+1] * nums[i+1]
        
        for i in range(0, len(nums)):
            res[i] = pref_sum[i] * suff_sum[i]
        
        return res
        
        

