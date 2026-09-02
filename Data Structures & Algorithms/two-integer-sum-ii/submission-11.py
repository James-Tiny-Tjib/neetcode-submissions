class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        # The idea is that there is only 1 solution, and that they're already in order
        # Start with this while loop
        while l < r:
            # Get Sum
            sum = numbers[l] + numbers[r]
            # If its equal break
            if sum == target:
                return [l+1,r+1]
            # Else if the sum is too large, decrease it by moving hte right pointer down
            elif sum > target:
                r -= 1
            # Else make the sum bigger by moving left pointer up
            else:
                l += 1
        