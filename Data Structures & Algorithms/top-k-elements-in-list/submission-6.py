class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq_dict = {}

        for n in nums:
            freq_dict[n] = freq_dict.get(n, 0) + 1
        
        freq_buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in freq_dict.items():
            freq_buckets[freq].append(num)
        
        result = []

        for i in range(len(nums), -1, -1):

            for n in freq_buckets[i]:

                if len(result) < k:
                    result.append(n)
                else:
                    return result
        
        return result
            
            
            
