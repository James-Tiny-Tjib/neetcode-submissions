from collections import defaultdict
class TimeMap:

    # Idea: Create a Dictionary to do the key thing
    # Then each key will correspond to a list where we just append
    def __init__(self):
        self.ht = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ht[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ht:
            return ""
        time_list = self.ht[key]
        l = 0
        r = len(time_list)-1
        res = 0

        while l <= r:

            mid = (l + r) // 2
            if time_list[mid][1] == timestamp:
                return time_list[mid][0]
            elif time_list[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if time_list[r][1] > timestamp:
            return ""
        return time_list[r][0]

# 4 and 6 are missing
# 4:
# 1 2 3 5 7 8 9 
# L     M     R
# L M R
#     L,M,R 
#     R L 

# 1 2 3 5 7 8 9
# L     M     R
#         L M R        
#         L,M,R
#       R L 