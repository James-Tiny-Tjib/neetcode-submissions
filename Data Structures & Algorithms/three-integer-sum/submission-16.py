class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Results Array
        res = []

        # Sort 
        self.heapsort(nums)

        # Iterate through list acting as a candidates for the first number in the triplet
        for i, n in enumerate(nums):

            # if the number is positive, the future numbers in the sorted list can't be sum up to 0, 
            # so we immediately break out of it. 
            if n > 0:
                break

            # To skip duplicates formed from different 1st triplet numbers (e.g. [-1, -1, -1, 0, 1]),
            # skip the outer loop iteration so that it
            if i>0 and n == nums[i - 1]:
                continue
            
            # Now start the l at i+1 (since i is the number being held constant), and r to the last element
            l = i + 1
            r = len(nums) - 1

            # Then do 2sum
            while l < r:
                # Whent he target is found
                if nums[i] + nums[l] + nums[r] == 0:

                    # Add it to result
                    res.append([nums[i], nums[l], nums[r]])

                    # To prevent duplications, we need to keep going until the next number 
                    # does not equal the same number at the OG l+1. 
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    # That while loop breaks on the last iteration num[l] 
                    # was the same, so we skip 1 more
                    l += 1

                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        
        return res

        


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
        