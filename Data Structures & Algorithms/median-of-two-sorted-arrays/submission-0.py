class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # The idea is simple: we find the total length of the list, and find the numbers from each of the list that contain
        # the left partition. Like if a list contained n items, we need the find the left n/2 items. The trick is we need to 
        # first x elements from nums1 and y elements from nums2 s.t. x + y = n/2. Finding how to break up x & y is what we 
        # use binary search for

        # Find the Total length
        len2 = (len(nums1) + len(nums2))

        # The one we're binary search has to be the shorter one
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        # Find the Half
        half = len2 // 2

        # Left and Right pointers for nums1
        # We want number of elements so we use len, not len - 1
        l = 0
        r = len(nums1)

        # The idea is this: assume nums1 has length k. we need to find x elements where the the first x elements of 
        
        while l <= r:  
            
            # Get the middle of the left
            mid = (l + r) // 2

            # Get y elements of nums2
            rmn_left_part = half - mid

            left1 = nums1[mid - 1] if mid > 0 else float("-inf")
            right1 = nums1[mid] if mid < len(nums1) else float("inf")

            left2 = nums2[rmn_left_part - 1] if rmn_left_part > 0 else float("-inf")
            right2 = nums2[rmn_left_part] if rmn_left_part < len(nums2) else float("inf")


            # Check if its valid:
            if left1 <= right2 and left2 <= right1:
                
                if len2 % 2 == 1:
                    return min(right1, right2)

                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

            else:
                if left1 > right2:
                    r = mid - 1
                else:
                    l = mid + 1

