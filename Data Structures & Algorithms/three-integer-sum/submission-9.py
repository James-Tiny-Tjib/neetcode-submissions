from bisect import bisect_right
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        result = []
        count = Counter(nums)
        zero_count = count.pop(0, 0)
        if zero_count > 2: # first zero case
            result.append([0, 0, 0])
        for num in count:
            if num < 0 and zero_count and -num in count: # all zero cases covered
                result.append([num, 0, -num])
            if not num & 1 and count.get((half := -(num >> 1)), 0) > 1: # check all duplicate cases (must be even)
                result.append([num, half, half] if num < 0 else [half, half, num])
        if len(count) < 3: # all duplicate cases are now done (and zeroes)
            return result
        uniques = sorted(count)
        smallest, largest = uniques[0], uniques[-1]
        if smallest > 0 or largest < 0: # if smallest and largest are same sign, no more left
            return result
        # smallest < num < largest
        # num < 0, -num * 2 < largest
        # num > -largest // 2
        start_search = -largest // 2 # rounds to -inf, should be inclusive so bisect_right since it rounded backwards: -2.5 -> -3 : should start at -2. -2 -> -2 should start at -1 (bisect_right)
        # smallest < num < largest
        # num > 0, -num * 2 > smallest
        # num < -smallest // 2
        end_search = -smallest // 2 # bisect_right since rounding down positive makes inclusive BUT we need exclusive for end in range: 5 // 2 -> 2 which is right but since end_range we want 1 after.
        start = bisect_right(uniques, start_search) if smallest < start_search else 1
        stop = bisect_right(uniques, end_search) if end_search < largest else len(uniques) - 1 # since stop is exclusive
        for i in range(start, stop):
            num = uniques[i]
            begin = bisect_right(uniques, -(num << 1)) if num < 0 else i + 1 # > num * 2 if neg, > if pos
            end = bisect_right(uniques, -smallest - num) # max it can be is -smallest - num, bisect_right since exclusive
            
            for right in uniques[begin:end]:
                if (left := -num - right) in count:
                    result.append([left, num, right])
        return result



        
        