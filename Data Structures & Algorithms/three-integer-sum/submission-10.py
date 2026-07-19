class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort the Array via heapsort T: O(nlog(n)) S: O(1)
        self.heapsort(nums)

        # Result Array
        result = []

        # Solution almost like 2 Sum but with an extra modification
        # Outer for loop takes 1 number (O(n))
        # Inner for loop does 2 sum on elements right of it, target being negative of outer number (O(n))
        
        for start_index, n, in enumerate(nums):

            # If smallest value (n) is positive, then we can stop looking
            if n > 0:
                break

            # Skip duplicate where the prev and curr number is the same
            # Cuz if they find the same pair that doesn't include the current,
            # then its a duplicate
            if start_index > 0 and n == nums[start_index-1]:
                continue

            # Start left point +1 from n
            l = start_index + 1
            # Start r always at the right
            r = len(nums) - 1

            # Ensure l < r (no need to have condition for l < r in the While True variation)
            while l < r:
                
                # Create Sum
                curSum = (nums[l] + nums[r] + n)
                # If greater r--, lesser l ++
                if curSum > 0:
                    r -=1
                elif curSum < 0:
                    l +=1
                else:
                    # Else curSum works and save result
                    result.append([nums[l], nums[r], n])

                    # Left Stimulation Variant

                    # Move Pointer
                    l += 1
                    # Remove Duplicate where l and l -1 are the same, r is the same
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    # # Right Stimulation Variant
                    # r -=1
                    # while nums[r] == nums[r + 1] and l < r:
                    #     r -= 1

        return result

            


    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def siftDown(self, nums, i, upper):
        """
        nums = the arr
        i = parent node
        upper = upper bound index that ignores the sorted partition of the array
        """
        while True:
            # Formulas to get parent's left and right children nodes
            l, r = i*2 + 1, i*2 + 2
            # Case 1: Children Nodes indices are less than upper
            # This Also means that that the parent has 2 children
            if max(l, r) < upper:
                # If the parent is bigger than children, break
                if nums[i] >= max(nums[l], nums[r]):
                    break
                # Else one of the children is biggger, get the larger
                elif nums[l] > nums[r]:
                    self.swap(nums, i, l)
                    # Reassign the parent to the new parent
                    i = l
                else:
                    self.swap(nums, i, r)
                    # Reassign the parent to the new parent
                    i = r
            
            # Case #2 Only Left Child Exists
            elif l < upper:
                if nums[l] > nums[i]:
                    self.swap(nums, i, l)
                    i = l
                else:
                    break

            # If No children exists, break
            else:
                break          


    def heapsort(self,nums):
        for j in range((len(nums)-2)//2, -1, -1):
            self.siftDown(nums, j, len(nums))
        
        for end in range (len(nums)-1, 0, -1):
            self.swap(nums, 0, end)
            self.siftDown(nums, 0, end)
        
    
    