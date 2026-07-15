class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = {}

        for n in nums:
            if freq_dict.get(n) is None:
                freq_dict[n] = 1
            else:
                 freq_dict[n] += 1

        sorted_dict = dict(sorted(freq_dict.items(), key = lambda item : item[1]))

        return list(sorted_dict.keys())[-k:]     