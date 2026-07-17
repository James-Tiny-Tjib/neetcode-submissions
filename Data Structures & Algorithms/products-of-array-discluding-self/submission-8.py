class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        len_nums = len(nums)
        left_product = [nums[0]] + [1] * (len_nums-1)
        right_product = [1] * (len_nums-1) + [nums[len_nums-1]]

        for i in range(1, len_nums):
            left_product[i] = nums[i] * left_product[i - 1]
        
        for i in range (len_nums-2, -1, -1):
            right_product[i] = nums[i] * right_product[i + 1]

        output = [right_product[1]] + ([0] * (len_nums-2)) + [left_product[len_nums-2]]

        for i in range(1, len_nums-1):
            output[i] = left_product[i-1] * right_product[i+1]

        print(left_product)
        print(right_product)
        return output
        
