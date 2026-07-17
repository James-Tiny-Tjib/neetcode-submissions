class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        len_nums = len(nums)
        output = [nums[0]] + [1] * (len_nums-1)

        for i in range(1, len_nums-1):
            output[i] = nums[i] * output[i - 1]

        output[len_nums-1] = output[len_nums - 2]
        print(output)

        right_product = nums[len_nums-1]

        for i in range(len_nums-2, 0, -1):
            output[i] = right_product * output[i-1]
            right_product *= nums[i]
        
        output[0] = right_product

        return output
        
