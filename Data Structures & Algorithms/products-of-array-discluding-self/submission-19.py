class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        num_0_index = -1
        total_product = 1

        # Iterate through numbers
        for i, n in enumerate(nums):
            
            # Check if 0
            if n == 0:
                # If its the first time (-1 unchanged), set it
                if num_0_index == -1:
                    num_0_index = i
                # Else this is the 2nd zero, return all 0's
                else:
                    return [0] * len(nums)
            else:
                total_product *= n
        
        
        # If 0 has been set, set all nums to 0, set index with 0 to total_product
        if num_0_index != -1:
            result = [0] * len(nums)
            result[num_0_index] = total_product
            return result
        # Else takes nums and divide it
        else:
            for i in range(len(nums)):
                nums[i] = int(total_product / nums[i])
            return nums


        
        